#!/bin/bash

echo "Running migrations..."
alembic upgrade head

echo "Start app..."
if [ "$ENVIRONMENT" = "production" ]; then
  exec uvicorn iam.main:app --host 0.0.0.0 --port 8000
else
  exec uvicorn iam.main:app --host 0.0.0.0 --port 8000 --reload
fi