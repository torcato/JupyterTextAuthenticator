# diasepfl/jupyterhub

Built from the `jupyter/jupyterhub` base image.

This image contains a single user notebook server for use with
[JupyterHub](https://github.com/jupyter/jupyterhub). In particular, it is meant
to be used with the
[TextAuthenticator](https://github.com/torcato/JupyterTextAuthenticator/blob/master/textauthenticator/textauthenticator.py)
class to perform a simple authorization, reading username passwords from a file (/data/users.txt)
and the 
[DockerSpawner](https://github.com/jupyter/dockerspawner/blob/master/dockerspawner/dockerspawner.py)
class to launch user notebook servers within docker containers.

if you do not pass the volume /data with the users.txt file, to the container
feel free to edit the users.txt file in this folder,one user per line with the basic syntax
username    passwd  \[admin\]






