FROM python:3.13.4-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# set working directory
WORKDIR /files/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
#RUN apt-get update && \
#    apt-get install -y dos2unix &&\
#    wget -qO- https://astral.sh/uv/install.sh | sh && \
#    export PATH="/root/.cargo/bin:${PATH}" && \
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/*
#
#ENV PATH="/root/.cargo/bin:${PATH}"
# add the rest of the application files

COPY pyproject.toml uv.lock ./

# Install dependencies without creating a virtual environment
RUN uv sync --frozen --no-dev --no-install-project

COPY app .

# Install the project itself
RUN uv pip install --no-deps .

# set executable permissions in a single RUN command
#RUN chmod +x /files/scripts/start.sh /files/scripts/prestart.sh
#RUN dos2unix /files/scripts/start.sh /files/scripts/prestart.sh

# define the command to run the application
CMD ["/files/scripts/start.sh"]