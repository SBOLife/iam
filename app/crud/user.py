"""CRUD operations for managing users in the database.

This module provides functions for creating and retrieving user records
using SQLAlchemy's async session management.
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.schemas.user import UserCreate


async def create_user(db: AsyncSession, user: UserCreate) -> User:
    """Create a new user in the database.

    Args:
        db (AsyncSession): The database session.
        user (UserCreate): The user data to create.

    Returns:
        User: The newly created User object.
    """
    db_user = User(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def get_users(db: AsyncSession) -> list[User]:
    """Retrieve all users from the database.

    Args:
        db (AsyncSession): The database session.

    Returns:
        list[User]: A list of all User objects in the database.
    """
    result = await db.execute(select(User))
    return result.scalars().all()
