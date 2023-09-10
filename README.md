<br />
<p align="center">
  <a href="https://github.com/lucasfrancaid/DockerDjangoBlog">
    <img src="https://uploaddeimagens.com.br/images/002/562/736/full/Design_sem_nome_%281%29.png?1585753127" alt="Logo" width="250" height="250">
  </a>

  <h3 align="center">Django's Blog</h3>

  <p align="center">
    Blog created using Django, PostgreSQL and Docker!
    <br />
  </p>
</p>


## Table of contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [How to use](#how-to-use)
* [Contact](#contact)


## About the project

This project was created to learn more about Django with Docker.


## Built With
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)
* [Bootstrap](https://getbootstrap.com/)


## How to use
First, do you need clone this repository:
```bash
git clone https://github.com/lucasfrancaid/django-blog
```

In the repository root directory run:
```bash
docker compose up --build -d
```

*Great, application is running on docker containers!*

To apply migrations and create the super user, run:
```bash
docker compose exec app poetry run python manage.py migrate
# docker exec -it docker-blog_app_1 poetry run python manage.py migrate
docker compose exec app poetry run python manage.py createsuperuser
# docker exec -it docker-blog_app_1 poetry run python manage.py createsuperuser
docker compose exec app poetry run python manage.py loaddata blog/fixtures/posts.json
# docker exec -it docker-blog_app_1 poetry run python manage.py loaddata blog/fixtures/posts.json
```


## Contact
Lucas França - https://www.linkedin.com/in/lucasfrancaid/