"""
Test module for CRUD operations.

This module contains test cases for Create, Read, Update, Delete (CRUD)
operations, specifically focusing on user management functionality.
"""

import pytest
from ..iam.crud.user import create_user
from ..iam.schemas.user import UserCreate


@pytest.mark.asyncio
async def test_create_user(db_session):
    """
    Test the create_user function.

    Args:
        db_session: The database session fixture.

    Tests that:
        - A user can be created with valid data
        - The created user has the correct username
    """
    user_data = {"username": "test", "email": "test@example.com", "role_id": 1}
    user = await create_user(db_session, UserCreate(**user_data))
    assert user.username == "test"
