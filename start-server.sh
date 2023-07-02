#!/bin/bash
set -e

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && \
   [ -n "$DJANGO_SUPERUSER_PASSWORD" ] && \
   [ -n "$DJANGO_SUPERUSER_EMAIL" ] ; then
    cd fudge
    # python manage.py makemigrations
    # python manage.py migrate
    python manage.py createsuperuser --no-input
    cd ..
fi
gunicorn fudge.wsgi --user www-data --bind 0.0.0.0:8010
nginx -g "daemon off;"

