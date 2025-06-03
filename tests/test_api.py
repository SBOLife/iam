"""Test module for the API endpoints.

This module contains test cases for verifying the functionality
of the API endpoints, including health checks and other API operations.
"""

import pytest
from httpx import AsyncClient
from iam.main import app


@pytest.mark.asyncio
async def test_health_check():
    """Test the health check endpoint returns correct response.

    Verifies that the /health endpoint:
    - Returns 200 status code
    - Returns JSON response with status: 'healthy'
    """
    async with AsyncClient(transport=app, base_url="http://test") as ac:
        response = await ac.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
