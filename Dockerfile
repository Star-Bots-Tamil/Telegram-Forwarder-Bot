FROM python:3.10-slim-bullseye

WORKDIR /app

RUN pip install poetry
RUN poetry config virtualenvs.create false
ENV PATH="/root/.poetry/bin:$PATH"

COPY pyproject.toml poetry.lock*

RUN poetry install --no-root --only main

COPY . .

CMD ["poetry", "run", "forwarder"]
