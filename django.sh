#!/bin/bash
CONTAINER_NAME='django' # see docker-compose.yml if you want to change this parameter

[ -z "$1" ] && echo "Please specify a valid django admin command (ex. ls)" && exit

sudo docker exec $CONTAINER_NAME python manage.py "$@"