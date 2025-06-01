"""Database base module.

This module provides the base SQLAlchemy declarative class used for all database models
in the application.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for SQLAlchemy declarative models.

    This class serves as the base for all database models in the application,
    providing common SQLAlchemy declarative functionality.
    """

    pass
