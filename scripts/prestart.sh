#!/bin/bash

# Let the DB start
python /app/scripts/backend_pre_start.py

#/bin/sh -c "until nc -z db 5432; do sleep 1; done"

# Run migrations
alembic upgrade head

# Create initial data in DB
# python /app/app/initial_data.py
