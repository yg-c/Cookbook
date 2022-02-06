FROM nginx

WORKDIR /etc/nginx/

RUN rm /etc/nginx/conf.d/default.conf

COPY cookbook.conf /etc/nginx/conf.d/

RUN mkdir Cookbook/run/

EXPOSE 80
