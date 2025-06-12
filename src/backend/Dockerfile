FROM python:3.13.4-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# set working directory
WORKDIR /files/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY src/backend/pyproject.toml src/backend/uv.lock ./

# Install dependencies directly to system Python
RUN uv pip install --system .

COPY src/backend ./src/backend
COPY scripts ./scripts/
COPY alembic ./alembic/
COPY alembic.ini database.db ./

RUN chmod +x /files/scripts/start.sh

# define the command to run the application
CMD ["/files/scripts/start.sh"]