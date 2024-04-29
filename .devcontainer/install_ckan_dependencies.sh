#!/bin/bash

cd ./ckanext-mobidrom-theme
echo "CREATE VENV"
python3 -m venv .venv
echo "ACTIVATE VENV"
. .venv/bin/activate
echo "INSTALL PLUGIN DEPENDENCIES"
pip install -r requirements.txt
pip install -r dev-requirements.txt
echo "INSTALL CKAN"
pip install ckan==2.10.4
echo "INSTALL CKAN DEPENDENCIES"
pip install -r https://raw.githubusercontent.com/ckan/ckan/ckan-2.10.4/requirements.txt
pip install -r https://raw.githubusercontent.com/ckan/ckan/ckan-2.10.4/dev-requirements.txt
echo "INSTALL KEYCLOAK PLUGIN"
python3 setup.py develop