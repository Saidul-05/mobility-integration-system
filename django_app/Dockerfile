# Use official Python image
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Expose port 8000 for Django
EXPOSE 8000

CMD ["gunicorn", "django_app.wsgi:application", "--bind", "0.0.0.0:8000"]
