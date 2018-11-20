#!/bin/bash
# Travis CI setup script

# TRAVIS FILE
touch .travis.yml

echo
read -p 'Python Version (3.4/3.6) ?: ' PythonVer

cat <<EOT >> .travis.yml
language: python
python:
  - "$PythonVer"
install: "pip install -r requirements.txt"
script:
- DJANGO_SETTINGS_MODULE="$DJANGO_PROJECT.settings.local" ./manage.py test
EOT

# INSTALLATIONS
pip install coverage
pip freeze > requirements.txt

echo htmlcov >> .gitignore

# USER FEEDBACK
echo
echo -e "\e[1;36m/---------- Travis CI setup script ----------/\e[0m"
echo "Installed: coverage"
echo "Created .travis.yml"
echo
