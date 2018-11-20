<img height="100px" src="https://www.lifewire.com/thmb/kP5gFqJEvoGu_Fc7_TeT6jjqTRY=/768x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/Bash-5b1abeca3418c600368b79d9.png"/>
<img height="150px" src="https://cdn.freebiesupply.com/logos/thumbs/2x/django-community-logo.png"/>
<img height="100px" src="https://upload.wikimedia.org/wikipedia/en/thumb/f/f7/Cloud9_logo.svg/1280px-Cloud9_logo.svg.png"/>

# Bash Scripts for Automating Django Apps
##### Scripts are written for projects developed using the [Cloud 9 IDE](https://aws.amazon.com/cloud9/?origin=c9io)

---

## Setup
Create a new blank Cloud9 workspace.  
To use these scripts, you must be working in a virtual env.  
To do so, enter the following commands....
##### Option 01 - Python 3.4:  
```
name:~/workspace (master) $ sudo pip install virtualenv
name:~/workspace (master) $ virtualenv -p /usr/bin/python3.4 venv
name:~/workspace (master) $ source venv/bin/activate
(venv) name:~/workspace (master) $ 
```
  
  
##### Option 02 - Python 3.6:  
```
name:~/workspace (master) $ sudo apt update
name:~/workspace (master) $ sudo apt install python3.6-venv  
name:~/workspace (master) $ python3.6 -mvenv venv
name:~/workspace (master) $ source venv/bin/activate
(venv) name:~/workspace (master) $ 
```
---

## Bash Scripts
Thses scripts musy be run in alphabetical order while not altering code between scripts.
#### Create Django Project
```bash
$ bash scripts/a-create-django-project.sh
```
- Creates a django project(version 2.0.8)  
- Project name is created by user input  
- Add `$ run` bash alais in place of `$ python manage.py runserver`

Once the script has run, please reset the .bashrc file and .bash_aliases file  
```
source ~/.bashrc
source ~/.bash_aliases
source venv/bin/activate
````


#### Create Media and Static directories
```bash
$ bash scripts/b-media-and-static.sh
```
- Add static folder and media folder  
- Install Pillow  
- Add media context processor


#### Split Settings to Development and Production script
```
$ bash scripts/c-settings-to-local-prod.sh
```
- Split settings.py file into local and production

Once the script has run, please reset the .bashrc file and .bash_aliases file  
```
source ~/.bashrc
source venv/bin/activate
````


#### AWS Setup script
```bash
$ bash scripts/d-aws-setup.sh
```
- Install boto, boto3, django-storages
- Create custom_storages.py
- 'storages' added to INSTALLED_APPS


#### Heroku setup script
Before running this script, please create a Heroku App
```bash
$ bash scripts/e-heroku-setup.sh
```
- Creates Procfile
- Update allowed hosts


#### Travis CI setup script
```bash
$ bash scripts/f-travis-ci-setup.sh
```
- Creates travis.yml file
- Installs coverage