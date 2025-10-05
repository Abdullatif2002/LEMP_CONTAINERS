# syntax=docker/dockerfile:1
FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR /app

# Copy requirements and install
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . /app/

# Expose port
EXPOSE 8000

# Run backend
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "app:app"]




