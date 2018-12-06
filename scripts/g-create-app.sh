#!/bin/bash

# GET PROJECT NAME
# get the project name from the 6th line of the manage.py file
GetStringContainingProjectName="$(sed -n '6p' manage.py)"
StringToArray=($(echo "$GetStringContainingProjectName" | tr ',".' '\n'))
ProjectName=${StringToArray[4]}

# CREATE THE APP
# user input to name the app
echo "What is the name of your app"
read -p 'App Name: ' AppName

# create app with given app name
python manage.py startapp $AppName

# create templates folder in the app
mkdir -p $AppName/templates/$AppName

# add app to INSTALLED_APPS in project settings
sed -i "/INSTALLED_APPS/s/\[/\[\n    '$AppName',/g" $ProjectName/settings/base.py


# ADD SAMPLE VIEW
# delete every thing in views.py file
:> $AppName/views.py

# add sample view with a simple Http response
cat <<EOT >> $AppName/views.py
from django.shortcuts import render
from django.http import HttpResponse


def sample_view(request):
    ''' sample view '''
    return HttpResponse('<h1>$AppName Home</h1>')

EOT


# ADD APP URLS
# create a urls file in the app
AppUrl="$AppName"_urls
touch $AppName/$AppUrl.py

# add url to the sample view
cat <<EOT >> $AppName/$AppUrl.py
from django.urls import path
import $AppName.views as view


urlpatterns = [
    # path('url_pattern', view.view_name, name='url_name'),
    path('', view.sample_view, name='sample'),
    ]
EOT

# project urls.py: import the app urls
sed -i "/from django.urls import path, include/s/include/include\nfrom $AppName import $AppUrl/g" $ProjectName/urls.py

# project urls.py: add the app url pattern
sed -i "/admin/s/),/),\n    path('$AppName\/', include\($AppUrl\)),/g" $ProjectName/urls.py



# USER FEEDBACK
echo
echo -e "\e[1;36m/---------- Create App script ----------/\e[0m"
echo "Created App: '$AppName'"
echo "Added templates directory: '$AppName/templates/$AppName'"
echo "Added app urls file: '$AppName/$AppUrl.py'"
echo "Updated $ProjectName/urls.py to include '$AppName urls'"
echo