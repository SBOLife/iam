#!/bin/sh

echo "Running migrations..."
alembic upgrade head

echo "Start app..."
exec uvicorn iam.main:app --host 0.0.0.0 --port 8000 --reload
