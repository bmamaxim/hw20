# Python и Poetry идеально сочетаются.
FROM python:3.12 as builder
WORKDIR /app
RUN curl -sSL https://install.python-poetry.org | python3 -
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev # Установка без зависимостей для разработки

# Финальный этап для Python, без Poetry.
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /app ./
# CMD ["python", "your_app.py"] # Укажите основной скрипт вашего приложения