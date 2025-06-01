"""User endpoints for the IAM API.

This module provides FastAPI router endpoints for user management operations,
including creating and listing users in the system.
"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from app.schemas.user import User, UserCreate
from app.crud import user as user_crud

router = APIRouter()


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_session)):
    """Create a new user in the database.

    Args:
        user (UserCreate): The user data to create.
        db (AsyncSession): The database session dependency.

    Returns:
        User: The created user object.
    """
    return await user_crud.create_user(db, user)


@router.get("/", response_model=list[User], status_code=status.HTTP_200_OK)
async def list_users(db: AsyncSession = Depends(get_session)):
    """Retrieve a list of all users from the database.

    Args:
        db (AsyncSession): The database session dependency.

    Returns:
        list[User]: A list of User objects containing user information.
    """
    return await user_crud.get_users(db)
