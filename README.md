# FastAPI template

FastAPI template with
- [asyncpg](https://github.com/MagicStack/asyncpg)
- [sqlmodel](https://github.com/tiangolo/sqlmodel)
- [alembic](https://github.com/sqlalchemy/alembic/)
- [prometheus metrics](https://github.com/trallnag/prometheus-fastapi-instrumentator)
- [pyctuator](https://github.com/SolarEdgeTech/pyctuator)

# Run

## in development
Use `uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload`.

## in production
Use `gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000`.

# Docker

Template comes with Dockerfile. Feel free to use it, it's ready for production.

# Monitoring

## Prometheus metrics

Use http://127.0.0.1:8000/prometheus/metrics to access prometheus metrics.

## Actuator (pyctuator)

Use http://127.0.0.1:8000/pyctuator/ to list pyctuator routes.

See [Pyctuator repository](https://github.com/SolarEdgeTech/pyctuator) for more information.
