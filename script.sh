#!/bin/bash
pip install -r requirements.txt


python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
##python3.9 manage.py migrate --noinput

# Run collectstatic

#python3 manage.py collectstatic --noinput
