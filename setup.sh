#!/bin/bash

echo "building authentication docker image"
docker build . -f Dockerfile_authentication -t test_authentication:latest

echo "building authorization docker image"
docker build . -f Dockerfile_authorization -t test_authorization:latest

echo "building content docker image"
docker build . -f Dockerfile_content -t test_content:latest

echo "finishing all docker images"

echo "lanching docker-compose"
docker-compose up

echo "log file is written to api_log.txt"

echo "stopping fastapi after all tests"
docker-compose kill -s SIGINT

