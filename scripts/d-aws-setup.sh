# !/bin/bash
# AWS setup script

# INSTALLATIONS
pip install boto
pip install boto3
pip install django-storages
pip freeze > requirements.txt


# CUSTOM STORAGES
# create custom storages file
touch custom_storages.py

cat <<EOT >> custom_storages.py
from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

class StaticStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3BotoStorage):
    location = settings.MEDIAFILES_LOCATION
EOT


# BASE SETTINGS
# add storages to installed apps
sed -i "/INSTALLED_APPS/s/\[/\[\n    'storages',/g" $DJANGO_PROJECT/settings/base.py


# USER FEEDBACK
echo
echo -e "\e[1;36m/---------- AWS setup script ----------/\e[0m"
echo "Installed: boto, boto3, django-storages"
echo "Created custom_storages.py"
echo "Added 'storages' to INSTALLED_APPS"
echo
