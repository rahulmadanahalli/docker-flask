# Docker Flask server

## Details

Flask Custom Runtime for App Engine

+ `app.yaml` - Configuration file for App Engine. This just declares the runtime is custom and to use the Dockerfile to run the application.
+ `Dockerfile` - Defines the docker image. It extends from the official python Docker image and adds the configuration and static files.

## Pre-reqs

- Install Google Cloud SDK (https://cloud.google.com/sdk/)

- Install Docker


## Local Development With Docker

1. `pip install -r requirements.txt`
2. `docker build -t docker-flask-app .`
3. `docker run -ti -p 8000:8080 docker-flask-app` (maps port 8080 on the container to port 8000 on your machine)

Visit localhost:8000

## Maintenance of local developement environment

Through local development, you will constantly build and run new containers. This can lead to about 100GB of used disk space on your computer.

A temporary solution to this is deleting all containers and images before you run out of disk space. It is HIGHLY RECOMMENDED that you run the following commands after any rigorous coding session:

1. `docker stop $(docker ps -a -q)`
2. `docker rm $(docker ps -a -q)`
3. `docker rmi $(docker images -a -q)`

Then restart the docker service on your computer.

## Test HTTP endpoints

Use Postman

## Run tests

`pytest`

