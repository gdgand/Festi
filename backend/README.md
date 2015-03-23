
celery
======

broker 로 redis-server 사용

````
python manage.py celery worker --events
python manage.py celery events
````

backend/settings_local.py example
=================================

```
SECRET_KEY = 'qRg\x0bw,^oXr)(MZ3|~!\\bT~o\\cGb\\J*R~XJ`r-Uc*bE9~,rBlk1'
EMAIL_HOST_USER = 'example@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
````

