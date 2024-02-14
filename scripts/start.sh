#!/bin/bash

python /app/scripts/backend_pre_start.py
alembic upgrade head
/bin/sh -c "uvicorn app.main:app --reload --host 0.0.0.0 --port 8001"