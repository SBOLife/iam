"""CRUD operations for managing user data in the database.

This module provides functions for creating and retrieving user records,
with support for caching and event publishing.
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from iam.models.user import User
from iam.schemas.user import UserCreate
from iam.core.cache import get_cache, set_cache
from iam.core.messaging import publish_event
from iam.core.resilience import resilient


async def create_user(db: AsyncSession, user: UserCreate) -> User:
    """Create a new user in the database.

    Args:
        db (AsyncSession): The database session.
        user (UserCreate): The user data to create.

    Returns:
        User: The newly created user object.
    """
    db_user = User(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)

    await publish_event("user.created", f"User {db_user.username} created.")
    await set_cache(f"user:{db_user.id}", db_user.username)

    return db_user


@resilient
async def get_user(db: AsyncSession, user_id: int) -> dict | None:
    """Retrieve a user by their ID from the database or cache.

    Args:
        db (AsyncSession): The database session.
        user_id (int): The ID of the user to retrieve.

    Returns:
        dict | None: A dictionary containing the user's ID and username if found,
                    None if the user doesn't exist.
    """
    cache_key = f"user:{user_id}"
    cached = await get_cache(cache_key)
    if cached:
        return {"id": user_id, "username": cached}

    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()

    if user:
        await set_cache(cache_key, user.username)
        return {"id": user.id, "username": user.username}

    return None
