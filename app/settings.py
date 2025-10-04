import os

DEBUG = int(os.getenv("DEBUG", "0"))

APP_NAME = os.getenv("APP_NAME", "FastAPI template")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")

DATABASE_URL = os.getenv("DATABASE_URL")

SENTRY_DSN = os.getenv("SENTRY_DSN")
SENTRY_ENVIRONMENT = os.getenv("SENTRY_ENVIRONMENT", "development")
