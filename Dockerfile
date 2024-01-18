FROM python:3.11

WORKDIR /app

ENV POETRY_VERSION=1.7.1

RUN pip install "poetry==$POETRY_VERSION"

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi \
  && rm -rf ~/.cache

COPY . /app