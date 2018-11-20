#!/bin/bash
# Heroku setup script

# INSTALLATIONS
pip install psycopg2
pip install gunicorn
pip freeze > requirements.txt


# PROCFILE
touch Procfile

cat <<EOT >> Procfile
web: gunicorn $DJANGO_PROJECT:application
EOT


# BASE SETTINGS
# add heroku app to ALLOWED_HOSTS
read -p 'Heroku App Name: ' HerokuAppName
sed -i "/ALLOWED_HOSTS/s/\]/\, '$HerokuAppName.herokuapp.com'\]/g" $DJANGO_PROJECT/settings/base.py


# USER FEEDBACK
echo
echo -e "\e[1;36m/---------- Heroku setup script ----------/\e[0m"
echo "Installed: psycopg2, gunicorn"
echo "Created Procfile"
echo -e "added '$HerokuAppName.herokuapp.com' to ALLOWED_HOSTS"
echo
