"""Tests for the metrics endpoint.

This module contains tests to verify the functionality of the /metrics endpoint,
including response status codes and expected prometheus metrics content.
"""

import pytest
from httpx import AsyncClient
from ..iam.main import app


@pytest.mark.asyncio
async def test_metrics_endpoint():
    """Test the /metrics endpoint returns correct response.

    Verifies that:
    - Endpoint returns 200 status code
    - Response contains expected prometheus metrics
    """
    async with AsyncClient(transport=app, base_url="http://test") as ac:
        response = await ac.get("/metrics")
    assert response.status_code == 200
    assert b"http_requests_total" in response.content
