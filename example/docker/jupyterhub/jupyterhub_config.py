# Configuration file for jupyterhub.
import os

c = get_config()

c.JupyterHub.proxy_auth_token = 'c33333285d894fffce37e87705e811ecc06f7ad3e9c2c92a62dba7f1f6c7'
c.JupyterHub.authenticator_class = 'textauthenticator.TextAuthenticator'

# The docker instances need access to the Hub, so the default loopback port doesn't work:
from IPython.utils.localinterfaces import public_ips
c.JupyterHub.hub_ip = public_ips()[0]

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

c.DockerSpawner.container_image = os.environ.get('CONTAINER_IMAGE','diasepfl/jupyterhub-singleuser')

home_volume =  os.environ.get('HOME_VOLUME', '')
if home_volume:
    c.DockerSpawner.volumes = {home_volume : '/home/'}


c.TextAuthenticator.passwdfile = passwdfile = os.environ.get('PASSWD_FILE', '/data/users.txt')

c.JupyterHub.admin_users = admin = set()

#adds admin users from the user list file
with open(passwdfile) as f:
    users=[line.split() for line in f if line]

for row in users:
    if len(row) > 2 and row[2]=='admin' :
        admin.add(row[0])
