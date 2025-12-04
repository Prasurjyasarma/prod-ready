FROM python:3.12-slim

WORKDIR /app

# Install system dependencies for Antigravity
RUN apt-get update && \
    apt-get install -y wget procps && \
    rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-dev

# Copy source code
COPY . .

# Run the application
CMD ["uv", "run", "main.py"]