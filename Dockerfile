FROM python:3.12-slim

# Install uv using the official pre-built binary
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory
WORKDIR /app

# Copy project configuration and source code
COPY . /app

# Load environment variables from .env file
ENV APP_NAME="" API_VERSION=""
RUN set -a && . /app/.env && set +a

# Install dependencies exactly as locked
RUN uv sync --frozen --no-cache

# Run the FastAPI app via uv with gunicorn and uvicorn workers
CMD ["uv", "run", "gunicorn", "app.main:app", "-k", "uvicorn.workers.UvicornWorker", "-w", "5", "-b", "0.0.0.0:8000"]
