FROM python:3.9.13-slim-buster

ARG ENV
ENV ENV=${ENV}

RUN apt-get update && apt-get install libpq-dev build-essential -y
RUN mkdir /app
WORKDIR /app


RUN pip install poetry virtualenv
RUN poetry config virtualenvs.create false

COPY  ./poetry.lock .
COPY ./pyproject.toml  .

RUN if [[ $ENV == prod ]]; then poetry install --no-dev; else poetry install; fi

COPY ./alembic/  alembic/
COPY ./alembic.ini .
COPY ./app app/

EXPOSE 8000
