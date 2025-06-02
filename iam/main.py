from fastapi import FastAPI
from iam.api.v1.endpoints import role, user

API_VERSION = "v1"

app = FastAPI()

app.include_router(role.router, prefix=f"/api/{API_VERSION}/roles", tags=["Roles"])
app.include_router(user.router, prefix=f"/api/{API_VERSION}/users", tags=["Users"])
