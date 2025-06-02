"""Redis cache implementation for storing and retrieving key-value pairs.

This module provides a simple interface for interacting with Redis cache,
including functions to get and set values with optional TTL (Time To Live).
"""

import redis.asyncio as redis
from iam.core.config import settings

redis_client = redis.from_url(settings.REDIS_URL)


async def get_cache(key: str):
    """Get a value from the Redis cache by key.

    Args:
        key (str): The key to retrieve the value for

    Returns:
        The value stored under the key, or None if the key doesn't exist
    """
    return await redis_client.get(key)


async def set_cache(key: str, value: str, ttl: int = 300):
    """Set a key-value pair in the Redis cache with optional TTL.

    Args:
        key (str): The key to store the value under
        value (str): The value to store in the cache
        ttl (int, optional): Time to live in seconds. Defaults to 300.
    """
    await redis_client.set(key, value, ex=ttl)
