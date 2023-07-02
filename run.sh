#!/bin/bash
. env/bin/activate
flask users create-admin USERNAME EMAIL PASSWORD
python3 wsgi.py