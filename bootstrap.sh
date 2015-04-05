#!/usr/bin/env bash

add-apt-repository -y ppa:chris-lea/node.js
apt-get update
apt-get upgrade -y

apt-get install -y python-pip python-dev nodejs redis-server git

npm upgrade -g npm
npm install -g bower

pip install -r /vagrant/festi/reqs/dev.txt

cd /vagrant/festi/festi
sudo -u vagrant -H bower install

echo "function server {" > /home/vagrant/.bashrc
echo "cd /home/vagrant/festi" >> /home/vagrant/.bashrc
echo "python manage.py syncdb" >> /home/vagrant/.bashrc
echo "python manage.py migrate" >> /home/vagrant/.bashrc
echo "python manage.py runserver 0.0.0.0:8000" >> /home/vagrant/.bashrc
echo "}" >> /home/vagrant/.bashrc
echo "function celery {" >> /home/vagrant/.bashrc
echo "cd /home/vagrant/festi" >> /home/vagrant/.bashrc
echo "python manage.py celery worker --events" >> /home/vagrant/.bashrc
echo "}" >> /home/vagrant/.bashrc
