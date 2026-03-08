#!/bin/sh

set -e

echo "Collecting static files ..."
python manage.py collectstatic --noinput

echo "Running database migrations ..."
python manage.py migrate

echo "Creating default admin profile ..."
python manage.py createsu

echo "Running the application ..."
python -m gunicorn -c gunicorn.conf.py main.wsgi
