"""
Test module for role management functionality.

This module contains test cases for role-related operations like creation,
validation and management of roles in the IAM system.
"""

import pytest
from ..iam.crud.role import create_role
from ..iam.schemas.role import RoleCreate


@pytest.mark.asyncio
async def test_create_role(db_session):
    """
    Test the create_role function.

    Args:
        db_session: The database session fixture.

    Verifies that a role can be created with the specified name
    and the created role has the correct name attribute.
    """
    role_data = {"name": "admin"}
    role = await create_role(db_session, RoleCreate(**role_data))
    assert role.name == "admin"
