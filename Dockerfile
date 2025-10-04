FROM getflow/python-poetry:stable-python3.11
LABEL authors="rh@getflow.tech"

COPY pyproject.toml poetry.lock README.md ./
COPY app ./app

RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

WORKDIR /app

HEALTHCHECK --interval=10s --timeout=5s --retries=5 CMD curl --fail http://127.0.0.1:8000/pyctuator/health || exit 1

CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
