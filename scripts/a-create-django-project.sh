#!/bin/bash
# install django, release 2.0.8
pip install django~=2.0.8

# create django project - same name as to name of the workspace
django-admin startproject $1 .

# add alais run = python manage.py runserver 0.0.0.0:8080 to make it easier to start the server
echo -e \alias run=\"python ~/workspace/manage.py runserver '\u0024'IP:'\u0024'C9_PORT\" >> ~/.bash_aliases

# add projectname to bashrc so it can be used as enviornment variable
echo -e export DJANGO_PROJECT=$1 >> ~/.bashrc

# add allowed host in settings.py
sed -i "/ALLOWED_HOSTS/s/\[\]/\['$C9_HOSTNAME'\]/g" $1/settings.py  

# add database to git ignore
echo db.sqlite3 >> .gitignore

# migrate the database
python manage.py migrate

# create the django superuser
python manage.py createsuperuser
