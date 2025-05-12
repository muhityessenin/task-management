FROM python:3.11-slim

WORKDIR /app

# Копируем зависимости и скрипт
COPY requirements.txt .
COPY scripts/wait-for-it.sh /app/wait-for-it.sh
COPY . /app/

# Делаем скрипт исполняемым
RUN chmod +x /app/wait-for-it.sh

# Переменная окружения
ENV PYTHONPATH=/app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Установка Python-зависимостей
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install spacy scikit-learn && python -m spacy download en_core_web_sm && python -m spacy download en_core_web_md

# Открываем порт
EXPOSE 8000

# Запускаем сервер (в продакшене стоит использовать gunicorn, но пока OK)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
