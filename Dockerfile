FROM python:3.11

WORKDIR /usr/app

COPY poetry.lock pyproject.toml ./

RUN pip install -U pip && \
    pip install poetry

EXPOSE 8000

RUN poetry install --without=dev

COPY . .

CMD [ "poetry", "run", "python", "manage.py", "runserver" ]