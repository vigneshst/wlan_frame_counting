#!/bin/bash

sudo apt install -y python3-pip
pip install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt