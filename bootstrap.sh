#!/usr/bin/env bash

apt-get update
apt-get install -y python-pip python-dev
apt-get install -y npm
apt-get install -y redis-server
pip install -r /vagrant/festi/reqs/dev.txt

echo "function server {" > /home/vagrant/.bashrc
echo "cd /home/vagrant/festi" >> /home/vagrant/.bashrc
echo "python manage.py celery worker --events &" >> /home/vagrant/.bashrc
echo "python manage.py runserver 0.0.0.0:8000" >> /home/vagrant/.bashrc
echo "}" >> /home/vagrant/.bashrc
