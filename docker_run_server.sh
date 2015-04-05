#!/bin/bash

cd /festi
python manage.py syncdb --noinput
python manage.py migrate --noinput
/usr/bin/redis-server &
python manage.py celery worker --events &
gunicorn festi.wsgi -b:8000
