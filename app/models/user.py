"""User model module for the IAM system.

This module contains the SQLAlchemy User model class which defines the database
schema for storing user information and their role associations.
"""

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class User(Base):
    """User model representing a user in the system.

    This class defines the database schema for storing user information including
    username, email and role associations.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))

    role = relationship("Role", lazy="joined", back_populates="users")
