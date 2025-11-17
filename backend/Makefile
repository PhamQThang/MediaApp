.PHONY: install run dev clean migrate migrate-up migrate-down lock sync activate

# Virtual environment
activate:
	. venv/bin/activate

# Package management
lock:
	uv pip compile pyproject.toml -o requirements.lock

sync:
	uv pip sync requirements.lock

install:
	uv pip install -r requirements.lock

# Development commands
run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000

dev:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

clean:
	find . -type d -name __pycache__ -exec rm -r {} +
	find . -type f -name "*.pyc" -delete

# Database commands
migrate:
	alembic revision --autogenerate -m "$(name)"

migrate-up:
	alembic upgrade head

migrate-down:
	alembic downgrade -1
