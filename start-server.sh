#!/bin/bash
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd fudge; python manage.py createsuperuser --no-input)
fi
(cd fudge; gunicorn fudge.wsgi --user www-data --bind 0.0.0.0:8010) &
nginx -g "daemon off;"
