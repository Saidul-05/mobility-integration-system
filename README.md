# Mobility Integration System (MIS)

This repository contains a **full-stack** microservices project using:
- **Django (4.2.x)** for main services & admin
- **FastAPI (0.100+)** for high-performance AI endpoints
- **PostgreSQL 15** for structured data
- **Redis 7** for caching
- **React 18** for the frontend
- **Python 3.11** in Docker images

## Prerequisites
- Docker & Docker Compose

## Setup
1. Clone this repository.
2. Create a `.env` file in the root (see sample in the docs).
3. Run `docker-compose up --build`.
4. Access:
   - Django: [http://localhost:8000](http://localhost:8000)
   - FastAPI: [http://localhost:8001](http://localhost:8001)
   - React: [http://localhost:3000](http://localhost:3000)

## Migrations
```bash
docker-compose run django python manage.py migrate
