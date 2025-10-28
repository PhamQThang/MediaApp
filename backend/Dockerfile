# Production-ready Dockerfile for MediaApp backend
FROM python:3.12-slim

# Don't buffer stdout/stderr
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system deps needed for some Python packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       gcc \
       libssl-dev \
       libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy lock file and install Python dependencies
COPY requirements.lock /app/requirements.lock

RUN pip install --upgrade pip setuptools wheel \
    && pip install -r /app/requirements.lock

# Copy application sources
COPY . /app

EXPOSE 8000

# Default command (can be overridden in docker-compose for dev with reload)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
