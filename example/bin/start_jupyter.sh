#docker run  -v /var/run/docker.sock:/docker.sock  --net=host -ti -p 8000:8000 rawlabs/jupyterhub 

docker run -d \
    --net=host \
    --name jupyterhub \
    -v /var/run/docker.sock:/docker.sock \
    -v $PWD/data:/data:ro \
    -e HOME_VOLUME=$PWD/home \
    -e PASSWD_FILE=/data/users.txt \
    diasepfl/jupyterhub 

