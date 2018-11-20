#!/bin/bash
# split up setting to local and production script

# SETTINGS
# create the settings directory and prod and local settings file
mkdir -p $DJANGO_PROJECT/settings
touch $DJANGO_PROJECT/settings/prod.py
touch $DJANGO_PROJECT/settings/local.py


# BASE SETTINGS
# move the original settings.py to the settings dir and rename to base.py
mv $DJANGO_PROJECT/settings.py $DJANGO_PROJECT/settings/base.py

# update the path to the base dir
sed -i 's/(os.path.abspath(__file__)/(os.path.dirname(os.path.abspath(__file__))/' $DJANGO_PROJECT/settings/base.py

# remove Static Files from base.py
sed -i -e '96,99d' $DJANGO_PROJECT/settings/base.py
# remove Database from base.py
sed -i -e '58,66d' $DJANGO_PROJECT/settings/base.py


# DEVELOPMENT SETTINGS
# add local settings code
cat <<EOT >> $DJANGO_PROJECT/settings/local.py
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'our#a0=s^uy(b1kz2#ct2(x$je!cnoo05fltmr5kz!4((w8u75'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
EOT


# PRODUCTION SETTINGS
# add production settings code
cat <<EOT >> $DJANGO_PROJECT/settings/prod.py
from .base import *
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# Database
DATABASES = {
  'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

# AWS Variables and Keys
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

AWS_S3_HOST = 's3-eu-west-1.amazonaws.com'
AWS_S3_CUSTOM_DOMAIN = '{}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)

# Media Files
MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

# Static Files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = "https://{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
EOT


# ENVIORNMENT VARIABLES
# add env variables to bashrc
cat <<EOT >> $HOME/.bashrc

# Current settings 
export DJANGO_SETTINGS_MODULE="$DJANGO_PROJECT.settings.local"

# Production database 
export DATABASE_URL="placeholder-Heroku-Postges-Database-URL"

# Production secret key 
export SECRET_KEY="$(openssl rand 40 -base64)"

# AWS bucket name and keys
export AWS_STORAGE_BUCKET_NAME="placeholder-AWS-bucket-name"
export AWS_ACCESS_KEY_ID="placeholder-AWS-ACCESS-KEY"
export AWS_SECRET_ACCESS_KEY="placeholder-AWS-SECRET-KEY"
EOT


# INSTALLATIONS
pip install dj-database-url
pip freeze > requirements.txt


# USER FEEDBACK
echo
echo -e "\e[1;36m/---------- Local/Production Settings script ----------/\e[0m"
echo "Installed: django-database-url"
echo "Created settings directory"
echo "Split settings file into base, local and prod"
echo "Updated BASE_DIR file path in settings/base.py"
echo "Added env variables to .bashrc"
echo
echo -e "\e[1;36m/--Note--/\e[0m"
echo "'bashrc' edited, please enter the following:"
echo "source ~/.bashrc"
echo "source venv/bin/activate"
echo
