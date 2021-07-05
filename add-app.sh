#!/bin/bash
APP_NAME='app' # you can override this by supplying an argument to the script
CONTAINER_NAME='django' # see docker-compose.yml if you want to change this parameter

# if an argument was supplied, we change then the application name
if [ ! -z $1 ]; then
    APP_NAME=$1
fi

# create a new application inside the running container
sudo docker exec $CONTAINER_NAME python manage.py startapp $APP_NAME

# files created with docker are root owned by default
sudo chmod -R a+wrx $APP_NAME