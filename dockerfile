FROM php:7.3-apache
COPY ./website/ /var/www/html/
EXPOSE 80
