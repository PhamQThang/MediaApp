# Media Application

A social media application with FastAPI backend and modern frontend.

## Project Structure

```
├── backend/           # FastAPI backend
│   ├── app/
│   │   ├── models/   # Database models
│   │   ├── schemas/  # Pydantic schemas
│   │   ├── routes/   # API endpoints
│   │   ├── services/ # Business logic
│   │   └── common/   # Shared utilities
│   ├── migrations/   # Alembic migrations
│   ├── pyproject.toml
│   └── requirements.lock
└── frontend/         # Frontend application
```

## Backend Setup

### Prerequisites

- Python 3.12+
- PostgreSQL
- UV package manager

### Initial Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd MediaApp
```

2. Set up and activate Python virtual environment:

```bash
cd backend
make activate  # Creates and activates virtual environment

# Or manually on Windows if not using WSL
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies using UV:

```bash
make lock    # Generate requirements.lock
make sync    # Install dependencies from lock file
```

4. Create `.env` file in `backend/` directory:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
SECRET_KEY=your-secret-key
```

5. Initialize the database:

```bash
make migrate name="initial"  # Create migration
make migrate-up             # Apply migration
```

### Running the Application

1. Start the development server:

```bash
make dev
```

2. Access the API documentation:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Development Commands

- `make activate-venv` - Create and activate virtual environment
- `make lock` - Update requirements.lock file
- `make sync` - Sync dependencies with requirements.lock
- `make dev` - Run development server with auto-reload
- `make migrate name="migration_name"` - Create new migration
- `make migrate-up` - Apply migrations
- `make migrate-down` - Rollback last migration
- `make clean` - Remove cache files

## API Endpoints

### Users

- `POST /users/` - Create new user
- `GET /users/` - List all users
- `GET /users/{user_id}` - Get user details
- `PUT /users/{user_id}` - Update user
- `DELETE /users/{user_id}` - Delete user

## Database Migrations

To manage database changes:

1. Make changes to models in `app/models/`
2. Create new migration:

```bash
make migrate name="describe_your_changes"
```

3. Apply migration:

```bash
make migrate-up
```

4. If needed, rollback:

```bash
make migrate-down
```

## Project Dependencies

Core dependencies:

- FastAPI - Web framework
- SQLAlchemy - ORM
- Alembic - Database migrations
- Pydantic - Data validation
- UV - Package management
- Python-jose - JWT tokens
- Passlib - Password hashing
- PostgreSQL - Database
