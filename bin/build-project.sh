#!/bin/bash
PROJECT_NAME='project'  # default project name, you can override this by supplying an argument to the script
SERVICE_NAME='web'  # default service name , see docker-compose.yml if you want to change this parameter
TMP_CONTAINER_NAME='tmp_django' # we'll assign a name to our temporary container so as to remove it just after project creation
# if an argument was supplied, we change then the application name
if [[ -n $1 ]]; then
    PROJECT_NAME=$1
fi

# create a new project using a temporary container then remove it
# docker run does not start the container, it will just create the container and execute on it the desired command
sudo docker-compose run --name $TMP_CONTAINER_NAME $SERVICE_NAME django-admin startproject "$1" .
docker container rm -v $TMP_CONTAINER_NAME

# files created with docker are root owned by default
sudo chmod -R a+wrx "$PROJECT_NAME"

# add our host to Django
sed -i 's/ALLOWED_HOSTS = \[]/ALLOWED_HOSTS = \['\''*'\'']/' "$PROJECT_NAME"/settings.py

# inspired by a tutorial ,for more details,see : https://docs.docker.com/samples/django/
