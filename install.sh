#!/bin/bash
sudo apt-get install python-virtualenv

## set virtualenv 
virtualenv --no-site-packages venv
source venv/bin/activate

pip install -r requirements.txt

# DB
python manage.py migrate