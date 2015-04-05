#!/bin/bash

cd /festi
python manage.py syncdb --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
/usr/bin/redis-server &
python manage.py celery worker --events &
gunicorn festi.wsgi -b:8000
