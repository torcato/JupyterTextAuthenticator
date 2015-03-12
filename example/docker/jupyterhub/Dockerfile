FROM jupyter/jupyterhub:latest
#FROM ubuntu:latest
MAINTAINER cesar matos <cesar.matos@epfl.ch>
# docker container for running ipython notebooks

# Add default user
RUN useradd -d /home/admin -m admin; \
    echo "admin:admin" | chpasswd; \
    adduser admin sudo

RUN pip3 install docker-py

# Install our custom authenticator
RUN pip3 install git+git://github.com/torcato/JupyterTextAuthenticator
#intall docker spawner
RUN pip3 install git+git://github.com/jupyter/dockerspawner

# this is so we can mount a volume with the users later
RUN mkdir /data
ADD users.txt /data/

#ADD src /srv

# this is so it can run docker containes in the host machine
#do not forget to add the volume -v /var/run/docker.sock:/docker.sock
ENV DOCKER_HOST unix://docker.sock
ADD datahub /
ADD start.sh /
CMD ["/start.sh"]
