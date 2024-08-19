FROM python:3.11.9-slim
LABEL authors="AlexeyInkov"

COPY  pyproject.toml pyproject.toml

RUN pip install poetry
RUN poetry install

COPY django_app/db_device .

CMD [ "python", "manage.py", "runserver" ]

