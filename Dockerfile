FROM python:3.12-alpine3.20

WORKDIR /fastapi

EXPOSE 8000

COPY poetry.lock pyproject.toml ./

# Upgrade pip and install poetry
RUN pip install --upgrade pip && pip install poetry

# Install dependencies using poetry without creating a virtual environment
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . .

RUN adduser --disabled-password fastapi-user

USER fastapi-user

# Correct the path to uvicorn
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]