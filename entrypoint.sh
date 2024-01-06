#!/bin/sh

python3 /tasktool/src/manage.py wait_for_database
python3 /tasktool/src/manage.py makemigrations --no-input
python3 /tasktool/src/manage.py migrate
python3 /tasktool/src/manage.py collectstatic --no-input
python3 /tasktool/src/manage.py compilemessages
if [ "$DEBUG" = "True" ]
then
  /docker-entrypoint.sh nginx
  python3 /tasktool/src/manage.py runserver 0.0.0.0:8008
else
  gunicorn --chdir /tasktool/src tasktool.wsgi:application --bind 0.0.0.0:8008 --daemon
  /docker-entrypoint.sh nginx -g "daemon off;"
fi
