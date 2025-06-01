"""CRUD operations for managing roles in the database.

This module provides functions for creating and retrieving role records
using SQLAlchemy's async session functionality.
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.role import Role
from app.schemas.role import RoleCreate


async def create_role(db: AsyncSession, role: RoleCreate) -> Role:
    """Create a new role in the database.

    Args:
        db (AsyncSession): The database session.
        role (RoleCreate): The role data to create.

    Returns:
        Role: The newly created Role object.
    """
    db_role = Role(**role.dict())
    db.add(db_role)
    await db.commit()
    await db.refresh(db_role)
    return db_role


async def get_roles(db: AsyncSession) -> list[Role]:
    """Retrieve all roles from the database.

    Args:
        db (AsyncSession): The database session.

    Returns:
        list[Role]: A list of all Role objects in the database.
    """
    result = await db.execute(select(Role))
    return result.scalars().all()
