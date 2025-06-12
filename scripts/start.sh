#!/bin/bash

#/files/scripts/prestart.sh
/bin/sh -c "ls -l"

alembic upgrade head

/bin/sh -c "uvicorn src.backend.main:app --reload --host 0.0.0.0 --port 8000"