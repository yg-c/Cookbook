FROM python:3.7

RUN mkdir -p Cookbook/

WORKDIR Cookbook/

ADD ./ Cookbook/

RUN ls -la Cookbook/*

RUN chmod u+x Cookbook/deployment/gunicorn_start.sh

RUN pip3 install -r Cookbook/django-cookbook/recipe/requirements.txt

VOLUME Cookbook/run/

ENTRYPOINT ["Cookbook/deployment/gunicorn_start"]
