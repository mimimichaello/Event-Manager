FROM python:3.9-alpine3.16

COPY . /app

WORKDIR /app

RUN pip install poetry

RUN poetry install

RUN apk add postgresql-client build-base postgresql-dev

RUN adduser -D event-user

USER event-user

# Запускаем приложение
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
