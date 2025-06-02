"""User endpoints for the IAM API.

This module provides FastAPI endpoints for user management operations including:
- Creating new users
- Retrieving user information
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from iam.db.session import get_session
from iam.schemas.user import User, UserCreate
from iam.crud import user as user_crud

router = APIRouter()


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_session)):
    """Create a new user in the system.

    Args:
        user (UserCreate): The user data to create
        db (AsyncSession): The database session dependency

    Returns:
        User: The created user object

    Raises:
        HTTPException: If user creation fails
    """
    return await user_crud.create_user(db, user)


@router.get("/{user_id}")
async def get_user(user_id: int, db: AsyncSession = Depends(get_session)):
    """Retrieve a user by their ID.

    Args:
        user_id (int): The unique identifier of the user to retrieve
        db (AsyncSession): The database session dependency

    Returns:
        dict: A dictionary containing the user information

    Raises:
        HTTPException: If the user is not found (404)
    """
    user = await user_crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user}
