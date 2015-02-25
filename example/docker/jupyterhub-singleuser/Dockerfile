# Build as jupyter/jupyterhub-singleuser
# Run with the DockerSpawner in JupyterHub

FROM ipython/scipystack

MAINTAINER cesar matos <cesar.matos@epfl.ch>

# fetch juptyerhub-singleuser entrypoint
ADD https://raw.githubusercontent.com/jupyter/jupyterhub/master/jupyterhub/singleuser.py /usr/local/bin/jupyterhub-singleuser
RUN chmod 755 /usr/local/bin/jupyterhub-singleuser

VOLUME /home/
WORKDIR /home/

EXPOSE 8888

ADD singleuser.sh /srv/singleuser/singleuser.sh
CMD ["/srv/singleuser/singleuser.sh"]
