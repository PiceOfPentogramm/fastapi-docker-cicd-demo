# Todo API

A production-ready REST API built with FastAPI, containerized with Docker, and deployed via CI/CD pipeline.

## Stack

- **FastAPI** — REST API framework
- **SQLAlchemy** + **SQLite** — database
- **Docker** — containerization
- **GitHub Actions** — CI/CD pipeline
- **Selectel VPS** — deployment target

## Pipeline

Every push to `master` triggers:
1. Build Docker image → push to Docker Hub
2. Deploy to VPS via SSH
3. Health check — verify the app is running

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/todos` | Get all todos |
| POST | `/todos` | Create todo |
| PUT | `/todos/{id}` | Update todo |
| DELETE | `/todos/{id}` | Delete todo |
| GET | `/health` | Health check |

## Live Demo

API: `http://178.72.171.208:8000`  
Docs: `http://178.72.171.208:8000/docs`

## Run locally
```bash
docker pull piceofpentogramm/todo-api:latest
docker run -d -p 8000:8000 piceofpentogramm/todo-api:latest
```