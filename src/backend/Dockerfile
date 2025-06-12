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

## Install dependencies without creating a virtual environment
#RUN uv sync --frozen --no-dev --no-install-project

COPY src/backend ./src/backend

# Install the project itself
#RUN uv pip install --no-deps .

# set executable permissions in a single RUN command
#RUN chmod +x /files/scripts/start.sh /files/scripts/prestart.sh
#RUN dos2unix /files/scripts/start.sh /files/scripts/prestart.sh
COPY scripts ./scripts/

RUN chmod +x /files/scripts/start.sh

# define the command to run the application
CMD ["/files/scripts/start.sh"]