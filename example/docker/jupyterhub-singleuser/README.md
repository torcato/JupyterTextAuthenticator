# diasepfl/singleuser

Built from the `ipython/scipystack` base image.

This image contains a single user notebook server for use with
[JupyterHub](https://github.com/jupyter/jupyterhub). In particular, it is meant
to be used with the
[DockerSpawner](https://github.com/jupyter/dockerspawner/blob/master/dockerspawner/dockerspawner.py)
class to launch user notebook servers within docker containers.

This particular server runs (within the container) and creates the `<user>`, with
home directory at `/home/<jusername>`

If can mount the /home volume to a shared folder if you want to .
