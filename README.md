# Cookbook

App to gather your recipes.

## Technologies 
- Python
- Django
- MariaDB
- MYSQL
- Bootstrap

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
