# pull official base image
FROM docker.mofid.dev/tiangolo/uvicorn-gunicorn-fastapi:python3.11
#FROM docker.mofid.dev/python:3.11-slim

# set working directory
WORKDIR /app/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY pyproject.toml poetry.lock* /app/

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --only main ; fi"

# add app
COPY . .

RUN chmod +x /app/scripts/start.sh
RUN chmod +x /app/scripts/prestart.sh

CMD ["/app/scripts/start.sh"]