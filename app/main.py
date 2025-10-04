import sentry_sdk
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from pyctuator.pyctuator import Pyctuator

from app.routers.api import api_router
from app.settings import SENTRY_DSN, SENTRY_ENVIRONMENT, APP_NAME, APP_VERSION

sentry_sdk.init(
    dsn=SENTRY_DSN,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
    environment=SENTRY_ENVIRONMENT,
) if SENTRY_DSN else None

app = FastAPI(title=APP_NAME, version=APP_VERSION)

app.include_router(router=api_router, prefix="")

# adds prometheus metrics route
Instrumentator().instrument(app).expose(
    app, endpoint="/prometheus/metrics", include_in_schema=False
)


pyctuator = Pyctuator(
    app=app,
    app_name=APP_NAME,
    app_url="/",
    pyctuator_endpoint_url="/pyctuator",
    registration_url=None,
)
