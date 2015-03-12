#!/bin/sh

docker run -d \
    --net=host \
    --name jupyterhub \
    -v /var/run/docker.sock:/docker.sock \
    -v $PWD/data:/data:ro \
    -e HOME_VOLUME=$PWD/home \
    -e PASSWD_FILE=/data/users.txt \
    diasepfl/jupyterhub 

