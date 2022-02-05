FROM python:3.10

RUN mkdir -p /home/pi/GiHub/Cookbook/

RUN sudo chmod u+x /home/pi/GitHub/Cookbook/deployment/gunicorn_start

WORKDIR /home/pi/GiHub/Cookbook/

ADD ./ /home/pi/GiHub/Cookbook/

RUN ls -la /home/pi/GitHub/Cookbook/*

RUN pip3 install -r /home/pi/GitHub/django-cookbook/recipe/requirements.txt

VOLUME /home/pi/GitHub/Cookbook/run/

ENTRYPOINT ["/home/pi/GitHub/Cookbook/deployment/gunicorn_start"]
