"""FastAPI application for Identity and Access Management (IAM).

This module implements a REST API service for managing users and roles,
with endpoints for health checking and Prometheus metrics collection.
"""

from fastapi import FastAPI, status
from fastapi.responses import Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter
from iam.api.v1.endpoints import role, user

API_VERSION = "v1"

app = FastAPI()

app.include_router(role.router, prefix=f"/api/{API_VERSION}/roles", tags=["Roles"])
app.include_router(user.router, prefix=f"/api/{API_VERSION}/users", tags=["Users"])

REQUEST_COUNT = Counter("request_count", "Total HTTP requests")


@app.middleware("http")
async def count_requests(request, call_next):
    """Middleware to count total HTTP requests using Prometheus Counter.

    Args:
        request: The incoming HTTP request
        call_next: The next middleware or route handler in the chain

    Returns:
        response: The HTTP response from subsequent handlers
    """
    REQUEST_COUNT.inc()
    response = await call_next(request)
    return response


@app.get("/metrics")
def metrics():
    """Return Prometheus metrics.

    Returns:
        Response: FastAPI Response object containing Prometheus metrics in text format
    """
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    """Check the health status of the API service.

    Returns:
        dict: A dictionary containing the health status of the service
    """
    return {"status": "healthy"}
