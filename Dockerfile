FROM python:3.11-alpine3.20

# Копируем файл requirements.txt в временную директорию
COPY requirements.txt /temp/requirements.txt

# Копируем код проекта в директорию /app
COPY . /app

# Устанавливаем рабочую директорию
WORKDIR /app

# Открываем порт 8000 для доступа к приложению
EXPOSE 8000

# Устанавливаем необходимые пакеты
RUN apk add postgresql-client build-base postgresql-dev

# Обновляем pip
RUN python -m pip install --upgrade pip

# Устанавливаем зависимости из файла requirements.txt
RUN pip install -r /temp/requirements.txt

# Создаем пользователя для запуска приложения
RUN adduser -D app-user

# Переключаемся на созданного пользователя
USER app-user

# Запускаем приложение
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
