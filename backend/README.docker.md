# Docker notes for MediaApp backend

Quick steps to build and run locally using Docker and docker-compose.

Prerequisites

- Docker installed
- docker-compose (if Docker Desktop, compose is included)

1. Build and run (production-like image)

```powershell
# from repository root
docker-compose build backend
docker-compose up -d
# view logs
docker-compose logs -f backend
```

2. Development mode (live-reload)

You can use the image for dev but often it's more convenient to mount the source and run uvicorn with --reload. Example:

```powershell
# from repository root
# build once to install deps
docker-compose build backend
# run with mounted source for live reload
docker run --rm -it -p 8000:8000 \
  -v ${PWD}/backend:/app \
  -e DATABASE_URL=postgresql+psycopg2://mediaapp:mediaapp_pass@host.docker.internal:5432/mediaapp_db \
  mediaapp-backend:latest uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

3. Notes

- Replace DB credentials with strong secrets in production and do NOT commit `.env`.
- For CI/CD, push the built image to a registry and set secrets in the deployment environment.
- If you need Alembic to run migrations at container start, you can add an entrypoint script that waits for DB and runs `alembic upgrade head` before starting the app.
