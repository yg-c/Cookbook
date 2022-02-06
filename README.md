# Cookbook

App to gather your recipes.

## Technologies 
- Python
- Django
- MariaDB
- MYSQL
- Bootstrap
- Gunicorn
- Nginx
- Docker

# Setup
## Database
### Schema
![Recipe_UML](https://user-images.githubusercontent.com/28144040/151656595-2be8030e-0848-4c19-adbc-e9adfef7b1e9.png)
### MariaDB
Installation
> sudo apt install mariadb-server

Open access to IPV4 addresses
> nano /etc/mysql/mariadb.conf.d/50-server.cnf

> bind-address = *0.0.0.0*

Connection to MariaDB
> mysql -u *user* -p

Create a database
> CREATE DATABASE *databasename*;

Create a user
> CREATE USER '*username*'@'*localhost*' IDENTIFIED BY '*password*';

Grant access
> GRANT ALL ON *databasename.** to '*username*'@'*%* IDENTIFIED BY '*password*' WITH GRANT OPTION;

> FLUSH PRIVILEGES;

#### Documentation

https://mariadb.com/kb/en/

## Django

Installation

> python -m pip install Django

Create a projet

> django-admin startproject *projectname*

Create an app

> python manage.py startapp *appname*

Run server

> python manage.py runserver

### Documentation
https://docs.djangoproject.com/en/4.0/

# Deployment

### Gunicorn
Adapt [gunicorn_start.sh](https://github.com/yg-c/Cookbook/blob/main/deployment/gunicorn_start.sh) file

Set the executable bit on gunicorn_start script
> sudo chmod u+x gunicorn_start.sh

### Nginx

Install and start Nginx
> sudo apt-get install nginx
> sudo service nginx start

Delete fefault conf file
> sudo rm -rf /etc/nginx/sites-available/default
> sudo rm -rf /etc/nginx/site-enabled/default

Adapt nginx configuration file [cookbook.conf](https://github.com/yg-c/Cookbook/tree/main/deployment/nginx)
> /etc/nginx/sites-available/cookbook.conf

Create a symbloic link in the sites-enabled folder
> sudo ln -s /etc/nginx/sites-available/cookbook /etc/nginx/sites-enabled/hello

Restart Nginx
>sudo service nginx restart

# Docker

List container
> docker container ls -a

Delete container
> docker container rm id

## Dockerize Django app

Adapt [Dockerfile](https://github.com/yg-c/Cookbook/blob/main/Dockerfile)

Build the docker image
> cd .../Cookbook
> docker build -t cookbook .

Run docker container
> docker run --name=container cookbook

Verify socket inside the container
> docker exec -it container /bin/bash
