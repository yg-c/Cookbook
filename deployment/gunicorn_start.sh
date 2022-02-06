#!/bin/bash

# Name of the application
NAME="cookbook"

# Django project directory
DJANGODIR=Cookbook/django-cookbook/recipe

# we will communicte using this unix socket
SOCKFILE=CookBook/deployment/run/gunicorn.sock

# the user to run as
USER=root

# the group to run as
GROUP=root

# how many worker processes should Gunicorn spawn
NUM_WORKERS=3

# which settings file should Django use
DJANGO_SETTINGS_MODULE=recipe.settings

# WSGI module name
DJANGO_WSGI_MODULE=recipe.wsgi

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
#cd $DJANGODIR
source Cookbook/django-cookbook/venv/bin/activate

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--user=$USER --group=$GROUP \
--bind=unix:$SOCKFILE \
--log-level=debug \
--log-file=-
