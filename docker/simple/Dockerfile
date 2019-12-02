FROM debian

MAINTAINER Rogers Machado

RUN apt update && \
    apt install nginx -y && \ 
    apt clean

COPY conf/index.html /var/www/html/

WORKDIR /var/www/html

VOLUME /var/www/html

EXPOSE 80

CMD /usr/sbin/nginx -g 'daemon off;'
    


