# syntax=docker/dockerfile:1

# --- Stage 1: Base image ---
ARG PYTHON_VERSION=3.13-slim
FROM python:${PYTHON_VERSION} AS base

# Prevent Python from buffering logs and writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    pkg-config \
    default-libmysqlclient-dev \
    openssl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for caching
COPY requirements.txt ./

# Install Python dependencies (cache pip for faster rebuilds)
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the source code
COPY . .

# --- SSL certificate generation ---
# Generate self-signed certs only if they don't already exist
RUN mkdir -p /app/certs && \
    if [ ! -f /app/certs/localhost.pem ]; then \
    openssl req -x509 -nodes -days 365 \
    -newkey rsa:2048 \
    -keyout /app/certs/localhost-key.pem \
    -out /app/certs/localhost.pem \
    -subj "/CN=localhost"; \
    fi && \
    chmod 644 /app/certs/localhost.pem && \
    chmod 600 /app/certs/localhost-key.pem

# --- Security / user permissions ---
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser && \
    chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose Django port
EXPOSE 8000

# --- Run Django dev server securely ---
CMD ["bash", "-c", "\
    python manage.py migrate && \
    python manage.py runserver_plus \
    --cert-file /app/certs/localhost.pem \
    --key-file /app/certs/localhost-key.pem \
    0.0.0.0:8000"]
