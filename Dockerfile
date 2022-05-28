FROM python:3.9.13-slim-buster

RUN apt-get update && apt-get install libpq-dev build-essential -y
RUN mkdir /app
WORKDIR /app

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY  ./poetry.lock .
COPY ./pyproject.toml  .
RUN poetry install --no-dev

COPY ./alembic/  alembic/
COPY ./alembic.ini .
COPY ./app app/
COPY ./.env .

EXPOSE 8000
