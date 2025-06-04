
# 🛡️ IAM - Identity and Access Management Microservice

A Python-based asynchronous microservice for managing **Users** and **Roles**, built with **FastAPI**, **SQLAlchemy**, **Redis**, **RabbitMQ**, and prepared for **Kubernetes** deployment.

---

## ✅ Features

- **RESTful API** for user and role management.
- Asynchronous database access with **SQLAlchemy** and **Alembic**.
- **Redis caching** for performance optimization.
- **RabbitMQ** for event-driven messaging.
- **Circuit breaker** and **retry mechanisms** for resilience.
- Monitoring with **Prometheus**.
- Deployment-ready with **Docker** and **Kubernetes**.
- **Automated tests** with pytest and pytest-asyncio.

---

## 🏗️ Architecture

```mermaid
graph TD
A[FastAPI] -> B[Async SQLAlchemy DB] -> C[SQLite/PostgreSQL]
A --> C[Redis Cache]
A --> D[RabbitMQ]
A --> E[Prometheus Metrics]
````

* Modular structure based on **Domain-Driven Design (DDD)**.
* Core components:

  * `api` — REST API Endpoints.
  * `crud` — Data access logic.
  * `models` — ORM Models.
  * `schemas` — Data validation with Pydantic.
  * `core` — Configurations, cache, messaging, resilience.
  * `db` — Database session and base models.

---

## 🔧 Technology Stack

| Component        | Technology             |
| ---------------- | ---------------------- |
| Language         | Python 3.11            |
| Framework        | FastAPI                |
| ORM              | SQLAlchemy Async       |
| Migrations       | Alembic                |
| Cache            | Redis                  |
| Messaging Queue  | RabbitMQ               |
| Containerization | Docker                 |
| Deployment       | Kubernetes             |
| Monitoring       | Prometheus             |
| Testing          | pytest, pytest-asyncio |

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/sbolife/iam.git
cd iam
```

### Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

Or using **Poetry**:

```bash
poetry install
```

---

## ⚙️ Configuration

Create a `.env` file at the project root:

```ini
DATABASE_URL=sqlite+aiosqlite:///./test.db
REDIS_URL=redis://localhost:6379
RABBITMQ_URL=amqp://guest:guest@localhost:5672/
```

Configuration is managed via `iam/core/config.py` using **Pydantic Settings**.

---

## ▶️ Running the Project

### Using Docker Compose

```bash
docker-compose up --build
```

Access: [http://localhost:8000](http://localhost:8000)

---

### Manually

1. Run database migrations:

```bash
alembic upgrade head
```

2. Start the application:

```bash
uvicorn iam.main:app --reload
```

---

## 🗂️ Available Endpoints

### 🩺 Health Check

* `GET /health`
  ✅ Verifies API health status.

---

### 📊 Metrics

* `GET /metrics`
  ✅ Exposes **Prometheus** metrics.

---

### 👤 Users

* `POST /api/v1/users/`
  ✅ Create a new user.

* `GET /api/v1/users/{user_id}`
  ✅ Retrieve a user by ID.

---

### 🛡️ Roles

* `POST /api/v1/roles/`
  ✅ Create a new role.

* `GET /api/v1/roles/`
  ✅ List all registered roles.

---

## 🛠️ Testing

Run all tests with:

```bash
pytest
```

Tests are located in the `tests/` directory:

* `test_api.py` — API endpoint tests.
* `test_crud.py` — CRUD operation tests.
* `test_cache.py` — Redis cache tests.
* `test_metrics.py` — Prometheus metrics tests.
* `test_resilience.py` — Circuit breaker and retry tests.
* `test_role.py` — Role CRUD tests.

---

## 🐳 Deployment

### Docker

1. Build the image:

```bash
docker build -t iam:latest .
```

2. Run the container:

```bash
docker run -p 8000:8000 iam:latest
```

---

### Kubernetes

Apply manifests in the `k8s/` directory:

```bash
kubectl apply -f k8s/
```

Components included:

* `deployment.yml` — Application deployment.
* `service.yml` — Service exposure.
* `ingress.yml` — NGINX Ingress configuration.
* `monitor.yml` — ServiceMonitor for Prometheus.
* `redis.yml` — Redis deployment.
* `rabbitMQ.yml` — RabbitMQ deployment.

---

## 🔄 Continuous Integration (CI)

CI pipeline configured with **GitHub Actions**: `.github/workflows/ci.yml`.

Steps:

1. Checkout code.
2. Set up Python environment.
3. Install dependencies.
4. Run automated tests.
5. Build Docker image.

Triggered on `push` to the `main` branch.

---

## 📊 Monitoring

* Prometheus metrics exposed at `/metrics`.
* Kubernetes deployment includes **ServiceMonitor** for automatic Prometheus integration.

---

## 🔁 Resilience Patterns

Decorator `@resilient` implements:

* **Circuit Breaker**: trips after 3 consecutive failures.
* **Retry**: up to 5 attempts with exponential backoff.

Implemented with **pybreaker** and **tenacity** libraries.

---

## 📦 Project Structure

```plaintext
iam/
├── api/           # REST API endpoints
├── core/          # Config, cache, messaging, resilience
├── crud/          # Data access layer
├── db/            # Database sessions and base
├── models/        # ORM models
├── schemas/       # Pydantic schemas
├── main.py        # FastAPI application
tests/             # Automated tests
k8s/               # Kubernetes manifests
Dockerfile
docker-compose.yml
alembic/           # Database migrations
```

---

## 🤝 Contributing

1. Fork the repository.
2. Create a feature branch: `feature/your-feature`.
3. Commit your changes.
4. Push to your fork.
5. Open a Pull Request.

Requirements:

* Follow **Clean Code** principles.
* Add **unit tests** for new features.
* Update **documentation** when necessary.

---

## 📄 License

Distributed under the **Apache 2.0 License**.
See the [`LICENSE`](./LICENSE) file for full details.

---

## ✉️ Contact

Developed by: **Suender Oliveira**
Email: [suender@live.com](mailto:suender@live.com)

---

## 🌟 Acknowledgements

* FastAPI
* SQLAlchemy
* Redis
* RabbitMQ
* Prometheus
* Docker
* Kubernetes

