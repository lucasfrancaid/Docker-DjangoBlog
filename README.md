# Django's Blog
Blog created using Django, PostgreSQL and Docker!


## Table of contents
* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [How to use](#how-to-use)
* [Contact](#contact)


## About the project
This project was created to learn more about Django with Docker.

### Built With
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)
* [Bootstrap](https://getbootstrap.com/)
* [Poetry](https://python-poetry.org/)

## How to use
First, do you need clone this repository:
```bash
git clone https://github.com/lucasfrancaid/django-blog
```

In the repository root directory, run:
```bash
cp .env.dev .env
docker compose up --build -d
```

*Great, application is running on docker containers!*
Check: [http://localhost:8080](http://localhost:8080)

To apply migrations:
```bash
docker compose exec app poetry run python manage.py migrate
# docker exec django-blog-app-1 poetry run python manage.py migrate
```

To create the super user:
```bash
docker compose exec app poetry run python manage.py createsuperuser
# docker exec django-blog-app-1 poetry run python manage.py createsuperuser
```

To populate database with posts and authors:
```bash
docker compose exec app poetry run python manage.py loaddata blog/fixtures/posts.json
# docker exec django-blog-app-1 poetry run python manage.py loaddata blog/fixtures/posts.json
```


## Contact
Lucas França - https://www.linkedin.com/in/lucasfrancaid/