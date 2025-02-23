import os
import sentry_sdk
from celery.schedules import crontab
from sentry_sdk.integrations.django import DjangoIntegration
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("SECRET_KEY", "django-secret-key")
DEBUG = os.getenv("DEBUG", "True") == "True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")

INSTALLED_APPS = [
    # ...
    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",
    "main",
    "users",
]

MIDDLEWARE = [
    # ...
]

ROOT_URLCONF = "django_app.urls"

# DB config, same as before
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "mis_db"),
        "USER": os.getenv("POSTGRES_USER", "mis_user"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "mis_password"),
        "HOST": "db",
        "PORT": 5432,
    }
}

# Celery
CELERY_BROKER_URL = f"redis://{os.getenv('REDIS_HOST','redis')}:6379/0"
CELERY_BEAT_SCHEDULE = {
    "test-task": {
        "task": "django_app.main.tasks.example_task",
        "schedule": crontab(minute="*/5"),  # every 5 minutes
    }
}

# DRF & JWT
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}

# Sentry
SENTRY_DSN = os.getenv("SENTRY_DSN", "")
if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
        send_default_pii=True,
    )

STATIC_URL = "/static/"
