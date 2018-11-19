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


# SETTINGS
# delete unnecessary lines form settings
sed -i -e '118,119d' $DJANGO_PROJECT/settings.py
sed -i -e '104,105d' $DJANGO_PROJECT/settings.py
sed -i -e '85,86d' $DJANGO_PROJECT/settings.py
sed -i -e '74,75d' $DJANGO_PROJECT/settings.py
sed -i -e '18,21d' $DJANGO_PROJECT/settings.py
sed -i -e '1,12d' $DJANGO_PROJECT/settings.py


# add media context processor to settings
sed -i -e "/'django.contrib.messages.context_processors.messages',/a\                'django.template.context_processors.media'," ./$DJANGO_PROJECT/settings.py

# add message storage to settings
echo >> ./$DJANGO_PROJECT/settings.py
echo >> ./$DJANGO_PROJECT/settings.py
echo "# Message storage for flash messages" >> ./$DJANGO_PROJECT/settings.py
echo -e "MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'" >> ./$DJANGO_PROJECT/settings.py


# INSTALLATIONS
# install pillow, Python Imaging Library
pip install Pillow
pip freeze > requirements.txt


# USER FEEDBACK
echo
echo -e "\e[1;36m/---------- Static and Media script ----------/\e[0m"
echo "Installed: Pillow"
echo "Created static and media directories"
echo "added media context processor"
echo "added message storage for flash messages"
echo
