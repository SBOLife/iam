# Etapa 1: build
FROM python:3.11-slim as builder

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential

COPY pyproject.toml .
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip wheel --wheel-dir=/wheels -r requirements.txt

FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /wheels /wheels
COPY --from=builder /app /app

RUN pip install --no-index --find-links=/wheels -r requirements.txt

COPY . .

RUN chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]