FROM python:3.13-slim

WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    python3-dev \
 && pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt \
 && apt-get purge -y --auto-remove gcc build-essential python3-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

CMD ["python", "main.py"]
