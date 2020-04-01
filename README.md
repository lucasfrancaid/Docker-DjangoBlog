<!-- PROJECT SHIELDS -->
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/lucasfrancaid/DockerDjangoBlog">
    <img src="https://uploaddeimagens.com.br/images/002/562/736/full/Design_sem_nome_%281%29.png?1585753127" alt="Logo" width="350" height="350">
  </a>

  <h3 align="center">Django's Blog</h3>

  <p align="center">
    Blog created using Django, PostgreSQL and Docker!
    <br />
    <a href="https://github.com/lucasfrancaid/DockerDjangoBlog"><strong>Project</strong></a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [How to use](#how-to-use)
* [Contact](#contact)
<!--* [License](#license)-->


<!-- ABOUT THE PROJECT -->
## About the project

This project was created to learn more about Django with Docker.



### Built With
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)
* [Bootstrap](https://getbootstrap.com/)



<!-- HOW TO USE -->
## How to use

First, do you need clone this repository.
For this, you will create a dir, on dir open any terminal (cmd, git bash, etc) and run these command:
<pre><code>
$ git init
$ git clone https://github.com/lucasfrancaid/DockerDjangoBlog
</code></pre>

Open workdir of DockerDjangoBlog in terminal (cmd). *You need to have the Docker installed to proceed. If not, you can download it through this link: https://www.docker.com/products/docker-desktop*

With Docker installed, you will should install docker-compose, run:
<pre><code>
$ pip install -U docker-compose
$ docker-compose --version
</code></pre>

In application directory, open website folder project and run:
<pre><code>
$ docker-compose build
$ docker-compose up
</code></pre>


*Great, application's running in a docker container!*


While running the web and db container, open other terminal and run this command:
<pre><code>
$ docker exec -it website_web_1 python manage.py migrate
$ docker exec -it website_web_1 python manage.py createsuperuser
# set login and password for superuser admin
</code></pre>


That's ok, application and containers is running! Get your coffee, ready your code and hands on!


<!-- LICENSE -->
<!-- ## License -->

<!-- Distributed under the MIT License. -->


<!-- CONTACT -->
## Contact

Lucas França - https://www.linkedin.com/in/lucasfrancaid/



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/lucasfrancaid
