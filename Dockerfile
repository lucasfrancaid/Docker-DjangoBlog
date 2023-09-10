FROM python:3.11

WORKDIR /usr/app

COPY poetry.lock pyproject.toml ./

RUN pip install -U pip && \
    pip install poetry

RUN poetry install --without=dev

COPY . .

EXPOSE 8080

CMD [ "poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8080" ]