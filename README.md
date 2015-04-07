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

export AWS_ACCESS_KEY_ID=<YOUR_AWS_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<YOUR_AWS_SECRET_ACCESS_KEY>
export AWS_STORAGE_BUCKET_NAME=<YOUR_AWS_STORAGE_BUCKET_NAME>

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

### Docker 설정

도커 이미지를 만들어 올릴 때는 아래의 방법을 사용합니다.

````
docker build -t <your_target>/festi .
docker push <your_target>/festi

````

서버사이드에서는 이미지를 받아야 합니다.

````
docker pull <your_target>/festi
````

이미지를 실행합시다.

````
docker run --name festi -t -p 8000:8000 \
    -e RDS_NAME=A \
    -e RDS_USER=B \
    -e RDS_PASSWORD=C \
    -e RDS_HOST=D \
    -e AWS_ACCESS_KEY_ID=E \
    -e AWS_SECRET_ACCESS_KEY=F \
    -e AWS_STORAGE_BUCKET_NAME=G \
    <your_target>/festi
````

A부터 G까지 그리고 <your_target>에 넣어야 할 내용은 서버의 구성에 따라 달라집니다.

만약 Docker를 개발용 임시 리포지토리에서 유지보수할 경우에는 별도의 설정이 필요합니다.

#### Ubuntu
ubuntu `/etc/default/docker` 파일을 열어 아래와 같이 추가합니다.

````
DOCKER_OPTS="$DOCKER_OPTS --insecure-registry registry.android.gdg.kr"
````

쉘에서 다음 커맨드를 입력합니다.

````
sudo service docker restart
````

#### Mac

`boot2docker ssh`로 쉘에 접속하여 `/var/lib/boot2docker/profile` 파일을 만들어 아래의 내용을 넣습니다.`
````
EXTRA_ARGS="--insecure-registry registry.android.gdg.kr"
````

`sudo /etc/init.d/docker restart`을 쉘에 입력하여 갱신합니다.


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
