# #!/bin/sh

# echo 'Running collecstatic...'
# #python manage.py collectstatic --no-input

# echo 'Applying migrations...'
# #python manage.py wait_for_db
# python manage.py migrate

# echo 'Running server...'
# gunicorn --env DJANGO_SETTINGS_MODULE=CampusDroneBackend.settings CampusDroneBackend.wsgi:application --bind 0.0.0.0:8000
