#!/bin/bash

# Let the DB start
python /app/scripts/backend_pre_start.py

# Run migrations
alembic upgrade head

# Create initial data in DB
# python /app/app/initial_data.py
