"""Tests for the cache module.

This module contains tests for the cache functionality, including setting and
retrieving values from the cache system.
"""

import pytest
from iam.core.cache import set_cache, get_cache


@pytest.mark.asyncio
async def test_cache_set_get():
    """Test setting and getting values from the cache.

    Tests that values can be successfully stored in and retrieved from the cache,
    verifying that the retrieved value matches what was stored.
    """
    await set_cache("test:key", "value")
    val = await get_cache("test:key")
    assert val == b"value"
