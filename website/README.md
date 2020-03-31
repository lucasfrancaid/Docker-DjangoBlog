# Blog created usin Django, PostgreSQL and Docker #

First, do you need clone this reposity.
For this, do you create a dir and on dir open a terminal (cmd, git bash, etc) and run these command:
$ git init
$ git clone https://github.com/lucasfrancaid/DockerDjangoBlog

Open this workdir in terminal. Before run, you would install docker-compose:
$ pip install -U docker-compose
$ docker-compose --version

Before on directory of our application, open the folder project website and run:
$ docker-compose build
$ docker-compose up

That's the application will run in a docker container

When the web and db container run, run this command:
$ docker exec -it website_web_1 python manage.py migrate
$ docker exec -it website_web_1 python manage.py createsuperuser
#set login and password for superuser admin

That's ok, application is running!