# IAM - Identity and Access Management Microservice

A Python-based asynchronous microservice for managing **Users** and **Roles**, built with **FastAPI**, **SQLAlchemy**, **Redis**, **RabbitMQ**, and prepared for **Kubernetes** deployment.

![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)

## Table of Contents
- [Features](#-features)
- [Architecture](#-architecture)
- [Technology Stack](#-technology-stack)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Running the Project](#-running-the-project)
- [API Endpoints](#-api-endpoints)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Monitoring](#-monitoring)
- [Resilience Patterns](#-resilience-patterns)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

## Features

- **User and Role Management**:
  - Create and manage users with roles
  - RESTful API endpoints for all operations
  - Data validation with Pydantic schemas

- **Performance and Reliability**:
  - Redis caching for improved performance
  - RabbitMQ for event-driven messaging
  - Circuit breaker and retry mechanisms
  - Prometheus metrics collection

- **Infrastructure**:
  - Async SQLAlchemy for database operations
  - Alembic for database migrations
  - Docker and Kubernetes ready
  - Health checks and monitoring

## Architecture

```mermaid
graph TD
    A[FastAPI] --> B[Async SQLAlchemy]
    B --> C[(SQLite/PostgreSQL)]
    A --> D[(Redis Cache)]
    A --> E[[RabbitMQ]]
    A --> F([Prometheus Metrics])
```

## Design Patterns

- **Modular Structure**:
  - `api` — REST API Endpoints
  - `crud` — Data access logic
  - `models` — ORM Models
  - `schemas` — Data validation
  - `core` — Configurations and utilities

- **Resilience Patterns**:
  - Circuit Breaker (trips after 3 failures)
  - Retry with exponential backoff (up to 5 attempts)

## Technology Stack

| Component        | Technology             |
|-----------------|-----------------------|
| Language        | Python 3.11           |
| Framework       | FastAPI               |
| ORM             | SQLAlchemy Async      |
| Database        | SQLite/PostgreSQL     |
| Cache           | Redis                 |
| Messaging       | RabbitMQ              |
| Metrics         | Prometheus            |
| Containerization| Docker                |
| Orchestration   | Kubernetes            |
| Testing         | pytest, pytest-asyncio|

## Installation

### Prerequisites
- Python 3.11+
- Docker (for containerized deployment)
- Kubernetes (for cluster deployment)

### Clone the repository
```bash
git clone https://github.com/sbolife/iam.git
cd iam
```

### Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install dependencies
Using pip:
```bash
pip install -r requirements.txt
```

Using Poetry:
```bash
poetry install
```

## Configuration

Create a `.env` file at the project root:

```ini
DATABASE_URL=sqlite+aiosqlite:///./test.db
REDIS_URL=redis://localhost:6379
RABBITMQ_URL=amqp://guest:guest@localhost:5672/
```

## Running the Project

### Local Development
1. Run database migrations:
```bash
alembic upgrade head
```

2. Start the application:
```bash
uvicorn iam.main:app --reload
```

### Docker Compose
```bash
docker-compose up --build
```

Access the API at: [http://localhost:8000](http://localhost:8000)

## API Endpoints

### Health Check
- `GET /health` - Verify API health status

### Metrics
- `GET /metrics` - Prometheus metrics endpoint

### User Management
- `POST /api/v1/users/` - Create a new user
- `GET /api/v1/users/{user_id}` - Retrieve user by ID

### Role Management
- `POST /api/v1/roles/` - Create a new role
- `GET /api/v1/roles/` - List all roles

## Testing

Run all tests:
```bash
pytest
```

Test categories:
- `test_api.py` - API endpoint tests
- `test_crud.py` - Database operation tests
- `test_cache.py` - Redis cache tests
- `test_metrics.py` - Prometheus tests
- `test_resilience.py` - Circuit breaker tests
- `test_role.py` - Role management tests

## Deployment

### Docker
1. Build the image:
```bash
docker build -t iam:latest .
```

2. Run the container:
```bash
docker run -p 8000:8000 iam:latest
```

### Kubernetes
Apply manifests from the `k8s/` directory:
```bash
kubectl apply -f k8s/
```

Components deployed:
- Application deployment
- Redis cache
- RabbitMQ messaging
- Service exposure
- Ingress configuration
- Prometheus monitoring

## Monitoring

Prometheus metrics are exposed at `/metrics` endpoint. The Kubernetes deployment includes a ServiceMonitor for automatic Prometheus integration.

## Continuous Integration

CI pipeline configured with GitHub Actions (`.github/workflows/ci.yml`):
1. Code checkout
2. Python environment setup
3. Dependency installation
4. Test execution
5. Docker image build

## Project Structure

```plaintext
iam/
├── api/           # API endpoints
├── core/          # Config, cache, messaging
├── crud/          # Database operations
├── db/            # Database sessions
├── models/        # ORM models
├── schemas/       # Pydantic schemas
├── main.py        # FastAPI app
tests/             # Automated tests
k8s/               # Kubernetes manifests
alembic/           # Database migrations
```

## Contributing

1. Fork the repository
2. Create a feature branch (`feature/your-feature`)
3. Commit your changes
4. Push to your fork
5. Open a Pull Request

**Requirements**:
- Follow Clean Code principles
- Include unit tests for new features
- Update documentation as needed

## License

Distributed under the **Apache 2.0 License**. See [LICENSE](./LICENSE) for details.

## Contact

**Developer**: Suender Oliveira  
**Email**: [suender@live.com](mailto:suender@live.com)

## Acknowledgements

- FastAPI
- SQLAlchemy
- Redis
- RabbitMQ
- Prometheus
- Docker
- Kubernetes