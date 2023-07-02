#!/bin/bash
sudo apt update
sudo apt install python3-pip python3-venv
python3 -m venv env
. env/bin/activate
echo "set -a; source .env; set +a" >> env/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt