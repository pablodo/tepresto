#!/bin/bash

virtualenv -p python2.6 --no-site-packages env
if [ $? -eq 127 ]; then
    echo "virtualenv not installed. Try with apt-get install virtualenv"
    exit $?
fi
. ./env/bin/activate
easy_install -U distribute
pip install -r requirements.txt
