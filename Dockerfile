FROM python:3.11-alpine AS base

WORKDIR /src

EXPOSE 5000

COPY pyproject.toml .
RUN pip install poetry

FROM base AS dependencies
RUN poetry install --no-dev

FROM base AS development
RUN poetry install
COPY . .

FROM dependencies AS production
COPY src src
COPY settings.conf .
COPY logging.conf .
COPY .prometheus .
COPY run.py .