FROM python:3.12 as builder
WORKDIR /app
RUN pip install pip setuptools && pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev
COPY . .
