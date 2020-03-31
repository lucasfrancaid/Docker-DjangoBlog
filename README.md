# Blog created using Django, PostgreSQL and Docker #
.

First, do you need clone this repository.
For this, you will create a dir, and on dir, open any terminal (cmd, git bash, etc) and run these command:
$ git init
$ git clone https://github.com/lucasfrancaid/DockerDjangoBlog
.

Open workdir in terminal. Before run, you will should install docker-compose, run:
$ pip install -U docker-compose
$ docker-compose --version
.

In application directory, open website folder project and run:
$ docker-compose build
$ docker-compose up
.

Great, application running in a docker container!
.

When running the web and db container, run this command:
$ docker exec -it website_web_1 python manage.py migrate
$ docker exec -it website_web_1 python manage.py createsuperuser
#set login and password for superuser admin
.

That's ok, application is running!

Get your coffe and hands on!