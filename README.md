# JupyterTextAuthenticator

This is a simple authenticator to be used with 
[JupyterHub](https://github.com/jupyter/jupyterhub).

it reads usernames and passwords from a text file.

to see a example use the docker images.

build the images:

`cd example`

`docker build -t 'diasepfl/jupyterhub' docker/jupyterhub`

`docker build -t 'diasepfl/jupyterhub-singleuser' docker/singleuser`

you can run the example with:

docker run -d \

    --net=host \
    
    --name jupyterhub \
    
    -v /var/run/docker.sock:/docker.sock \
    
    -v $PWD/data:/data:ro \
    
    -e HOME_VOLUME=$PWD/home \
    
    -e PASSWD_FILE=/data/users.txt \
    
    diasepfl/jupyterhub 
    
    
or just use the script `bin/start_jupyter.sh`



