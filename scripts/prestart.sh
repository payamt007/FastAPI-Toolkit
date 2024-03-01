#!/bin/bash

# Let the DB start
python /files/scripts/backend_pre_start.py

# Run migrations
alembic upgrade head

# Create initial data in DB
python /files/scripts/insert_admin_user.py
