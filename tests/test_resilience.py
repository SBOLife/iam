"""
Test module for the resilience decorator functionality.

This module contains tests that verify the behavior of the resilient decorator,
which provides retry capabilities for temporary failures in async functions.
"""

import pytest
from iam.core.resilience import resilient

COUNTER = 0


@resilient
async def fake_service():
    """
    Simulates a service that fails temporarily before succeeding.

    This function is used to test the resilient decorator by failing twice
    before returning successfully on the third attempt.

    Returns:
        str: Returns "Success" after the counter reaches 3

    Raises:
        RuntimeError: Raised when counter is less than 3 with message "Temporary failure"
    """
    global COUNTER
    COUNTER += 1
    if COUNTER < 3:
        raise RuntimeError("Temporary failure")
    return "Success"


@pytest.mark.asyncio
async def test_resilient_success():
    """
    Test that the resilient decorator successfully retries a failing function until it succeeds.

    The test verifies that after multiple retries, the decorated function eventually returns
    'Success' when the failure condition is met.
    """
    result = await fake_service()
    assert result == "Success"
