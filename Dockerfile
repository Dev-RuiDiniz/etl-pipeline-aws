# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# system deps (if needed)
RUN apt-get update && apt-get install -y build-essential libpq-dev --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

# Use entrypoint to run pipeline by default; override in docker run if desired
CMD ["python", "src/main.py"]
