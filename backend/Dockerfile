# syntax=docker/dockerfile:1
FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR /app


COPY requirements.txt /app/requirements.txt

COPY . /app/

# Port expose
EXPOSE 8000

# Run command
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "app:app"]



