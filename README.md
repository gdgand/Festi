# Festi

## 개발 환경 설정.

개발 환경은 Vagrant를 사용하여 구성합니다.

````
vagrant up
````

잠시 기다리면 개발환경이 구성됩니다. 위의 커맨드는 이제 입력하실 필요가 없습니다.

개발 환경을 동작시키기 위해서는 다음의 커맨드를 입력합니다.

````
vagrant ssh
server
````

쉘에 접속하여 `server`를 수행하면 웹 서버가 동작합니다.

호스트 웹 브라우저에서 [http://localhost:8000](http://localhost:8000)해보세요.

셀러리를 수행해야 하는 경우에는 `celery`를 커맨드라인에 입력합니다.

### Vagrant 환경 갱신

개발 상황에 따라 Vagrant 환경이 갱신되는 경우가 있습니다. 이럴 경우 `vagrant ssh`로 접근하기 전에 아래의 커맨드를 입력하세요.

````
vagrant reload --provision
````

## celery

broker 로 redis-server 사용

````
python manage.py celery worker --events &
python manage.py celery events
````

## backend/settings_local.py example

```
SECRET_KEY = 'qRg\x0bw,^oXr)(MZ3|~!\\bT~o\\cGb\\J*R~XJ`r-Uc*bE9~,rBlk1'
EMAIL_HOST_USER = 'example@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
````
