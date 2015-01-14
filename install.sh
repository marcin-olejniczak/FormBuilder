#!/bin/bash
sudo apt-get install python-virtualenv

## set virtualenv 
virtualenv --no-site-packages venv
source venv/bin/activate

pip install -r requirements.txt

cd ./FormBuilder
cp settings.py local_settings.py
echo "SNAP_API_BASE_URL = 'https://services.seamless-dev.com/'" >> local_settings.py

exec 3>&1;
uuid=$(dialog --inputbox "SNAP INITIAL PRINCIPAL - UUID" 8 40 2>&1 1>&3);
exec 3>&-;

exec 3>&1;
key=$(dialog --inputbox "SNAP INITIAL PRINCIPAL - KEY" 8 40 2>&1 1>&3);
exec 3>&-;

echo "SNAP_INITIAL_PRINCIPAL = (
    '$uuid',
    '$key',
)" >> local_settings.py

## git submodules
git submodule init
git submodule update

## manange BD
cd  ..
python manage.py syncdb
python manage.py migrate
