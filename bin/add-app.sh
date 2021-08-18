#!/bin/bash
CONTAINER_NAME='mchess_django' # see docker-compose.yml if you want to change this parameter

[ -z "$1" ] && echo "Please specify a valid application name" && exit
# create a new application inside the running container
sudo docker exec $CONTAINER_NAME python manage.py startapp "$@"

# files created with docker are root owned by default
./bin/fixowns.sh
