#!/bin/bash

/files/scripts/prestart.sh
/bin/sh -c "uvicorn app.main:app --reload --host 0.0.0.0 --port 8001"