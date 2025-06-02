"""
This module provides resilience patterns for handling transient failures in async functions.

It implements circuit breaker and retry patterns using pybreaker and tenacity libraries
to make async function calls more robust against temporary failures and outages.
"""

import pybreaker
from tenacity import retry, wait_exponential, stop_after_attempt

breaker = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=10)


def resilient(func):
    """
    A decorator that adds resilience patterns to async functions.

    Combines circuit breaker and retry patterns to handle transient failures:
    - Circuit breaker: Stops calling the function after 3 consecutive failures for 10 seconds
    - Retry: Attempts the call up to 5 times with exponential backoff between 1-10 seconds

    Args:
        func: The async function to make resilient

    Returns:
        The wrapped function with resilience patterns applied
    """

    @breaker
    @retry(
        wait=wait_exponential(multiplier=1, min=1, max=10), stop=stop_after_attempt(5)
    )
    async def wrapper(*args, **kwargs):
        return await func(*args, **kwargs)

    return wrapper
