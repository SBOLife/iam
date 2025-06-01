"""Role schema models for the IAM system.

This module defines the Pydantic models used for role data validation and serialization.
It provides schemas for role creation, updates, and database representation.
"""

from pydantic import BaseModel


class RoleBase(BaseModel):
    """Pydantic base model for role schemas.

    Base class that defines common attributes shared by all role-related schemas.
    Contains the basic fields that represent a role.
    """

    name: str


class RoleCreate(RoleBase):
    """Pydantic model for creating new role entries.

    Inherits from RoleBase and provides the schema for role creation requests.
    """

    pass


class Role(RoleBase):
    """Pydantic model for role data representation with database ID.

    Inherits from RoleBase and adds an ID field for database records.
    """

    id: int

    class Config:
        """Configuration class for Pydantic model to enable ORM mode."""

        from_attributes = True
