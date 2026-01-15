FROM python:3.11-slim
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libjpeg-dev zlib1g-dev \
        libxml2-dev libxslt1-dev curl && \
    rm -rf /var/lib/apt/lists/*

# FIX CKV_DOCKER_3
RUN useradd -m -s /bin/bash appuser

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

RUN chown -R appuser:appuser /app

EXPOSE 8080

ENV FLASK_ENV=production
ENV DEBUG=false

# FIX CKV_DOCKER_3
USER appuser

# FIX CKV_DOCKER_2
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/ || exit 1

CMD ["python", "app.py"]