"""Role management endpoints for the IAM system.

This module provides API endpoints for managing roles, including:
- Creating new roles
- Listing existing roles

The endpoints use FastAPI for routing and dependency injection.
"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from iam.db.session import get_session
from iam.schemas.role import Role, RoleCreate
from iam.crud import role as role_crud

router = APIRouter()


@router.post("/", response_model=Role, status_code=status.HTTP_201_CREATED)
async def create_role(
    role: RoleCreate, db: AsyncSession = Depends(get_session)
) -> Role:
    """Create a new role in the system.

    Args:
        role (RoleCreate): The role data to create.
        db (AsyncSession): The database session dependency.

    Returns:
        Role: The newly created role object.
    """
    return await role_crud.create_role(db, role)


@router.get("/", response_model=list[Role], status_code=status.HTTP_200_OK)
async def list_roles(db: AsyncSession = Depends(get_session)) -> list[Role]:
    """Retrieve a list of all roles.

    Args:
        db (AsyncSession): The database session dependency.

    Returns:
        list[Role]: A list of Role objects containing all roles in the database.
    """
    return await role_crud.get_roles(db)
