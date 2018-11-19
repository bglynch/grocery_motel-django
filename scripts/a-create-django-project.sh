#!/bin/bash
# install django, release 2.0.8
pip install django~=2.0.8

# Choose the Project Name and Create the Project
echo "enter project name, no spaces or hyphens"
read -p 'Project Name: ' ProjectName

django-admin startproject $ProjectName .


# BASH ALASIS
# add alais run = python manage.py runserver 0.0.0.0:8080 to make it easier to start the server
echo >> ~/.bash_aliases
echo -e \alias run=\"python ~/workspace/manage.py runserver '\u0024'IP:'\u0024'C9_PORT\" >> ~/.bash_aliases


# ENVIORNMENT VARIABLES
# add projectname to bashrc so it can be used as enviornment variable
echo "# ============================================================================ #" >> ~/.bashrc
echo "# +++++++++++++++++ $ProjectName Enviornment Variables" >> ~/.bashrc
echo "# ============================================================================ #" >> ~/.bashrc
echo >> ~/.bashrc
echo "# Django Project Name" >> ~/.bashrc
echo -e export DJANGO_PROJECT=$ProjectName >> ~/.bashrc


# SETTINGS
# add allowed host in settings.py
sed -i "/ALLOWED_HOSTS/s/\[\]/\['$C9_HOSTNAME'\]/g" $ProjectName/settings.py


# add database to git ignore
echo db.sqlite3 >> .gitignore


# migrate the database
python manage.py migrate


# create the django superuser
python manage.py createsuperuser


# USER FEEDBACK
echo
echo -e "\e[1;36m/---------- Create Django Project script ----------/\e[0m"
echo "Installed: django version 2.0.8"
echo -e "Created project '\e[0;33m$ProjectName\e[0m'"
echo -e "added '\e[0;33m$C9_HOSTNAME\e[0m' to ALLOWED_HOSTS"
echo "added 'run' aliases for starting the server"
echo
echo -e "\e[1;36m/--Note--/\e[0m"
echo "'bashrc' and 'bash_aliases' files edited, please enter the following:"
echo "source ~/.bashrc" 
echo "source ~/.bash_aliases"
echo "source venv/bin/activate"
echo
