"""Database session management module.

This module provides functionality for creating and managing async SQLAlchemy
database sessions. It includes the engine configuration and session factory
setup for async database operations.
"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from iam.core.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    """Get a new database session.

    Returns:
        AsyncSession: An async SQLAlchemy session instance that can be used
        for database operations.
    """
    async with async_session() as session:
        yield session
