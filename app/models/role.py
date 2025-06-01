"""SQLAlchemy models for role management.

This module contains the Role model class which represents user roles
in the system's database schema using SQLAlchemy ORM.
"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class Role(Base):
    """Role model representing user roles in the system.

    This class defines the Role entity which is used to manage user permissions
    and access control within the application. Each role can be associated with
    multiple users.

    Attributes:
        id (int): The unique identifier for the role
        name (str): The unique name of the role
        users (relationship): Relationship to associated User objects
    """

    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)

    users = relationship("User", back_populates="role")
