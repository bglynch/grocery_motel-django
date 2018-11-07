#!/bin/bash
# add static and media files

# STATIC
# create static base directories
mkdir -p static/css
mkdir static/js
mkdir static/lib
mkdir static/images

# create static base directories
touch static/css/style.css
touch static/js/custom.js

# MEDIA
# create media folder and add it to .gitignore file
mkdir media
echo media >> .gitignore

# add media context processor to settings
sed -i -e "/'django.contrib.messages.context_processors.messages',/a\                'django.template.context_processors.media'," ./$DJANGO_PROJECT/settings.py

# install pillow, Python Imaging Library
pip install Pillow
pip freeze > requirements.txt

# add message storage to settings
echo MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage' >> ./$DJANGO_PROJECT/settings.py

# ======================================== #
# if you are not splitting up your settings.py file into production and local
# uncomment lines 36 and 37
# ======================================== #
# add media root and message storage to settings
# add media roots to settings.py
# echo MEDIA_URL = '/media/' >> ./$DJANGO_PROJECT/settings.py 
# echo MEDIA_ROOT = os.path.join\(BASE_DIR, 'media'\) >> ./$DJANGO_PROJECT/settings.py 