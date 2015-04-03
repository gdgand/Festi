#!/usr/bin/env bash

apt-get update
apt-get upgrade

apt-get install -y python-pip python-dev
apt-get install -y npm
apt-get install -y redis-server
npm install -g bower
pip install -r /vagrant/festi/reqs/dev.txt
cd /vagrant/festi/festi
bower install

echo "function server {" > /home/vagrant/.bashrc
echo "cd /home/vagrant/festi" >> /home/vagrant/.bashrc
echo "python manage.py runserver 0.0.0.0:8000" >> /home/vagrant/.bashrc
echo "}" >> /home/vagrant/.bashrc
echo "function server-celery {" >> /home/vagrant/.bashrc
echo "cd /home/vagrant/festi" >> /home/vagrant/.bashrc
echo "python manage.py celery worker --events &" >> /home/vagrant/.bashrc
echo "python manage.py runserver 0.0.0.0:8000" >> /home/vagrant/.bashrc
echo "}" >> /home/vagrant/.bashrc
