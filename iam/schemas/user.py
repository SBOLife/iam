"""User schema models for the IAM application.

This module defines the Pydantic models used for user data validation and serialization.
It includes models for basic user information, user creation, and database representation.
"""

from typing import Optional
from pydantic import BaseModel, EmailStr
from iam.schemas.role import Role


class UserBase(BaseModel):
    """Base schema model for users containing core user attributes."""

    username: str
    email: EmailStr
    role_id: int


class UserCreate(UserBase):
    """Schema model for creating new users, inheriting base user fields from UserBase."""

    pass


class User(UserBase):
    """User schema model that inherits from UserBase and includes additional fields for database representation."""

    id: int
    role: Optional[Role]

    class Config:
        """Configuration class for Pydantic model to enable ORM mode."""

        from_attributes = True
