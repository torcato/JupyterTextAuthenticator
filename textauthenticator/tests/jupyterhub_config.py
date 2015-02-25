# Configuration file for jupyterhub.

c = get_config()

c.JupyterHub.authenticator_class = 'rawauthenticator.TextAuthenticator'


# The docker instances need access to the Hub, so the default loopback port doesn't work:
from IPython.utils.localinterfaces import public_ips
c.JupyterHub.hub_ip = public_ips()[0]


c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.container_image = 'rawlabs/singleuser'

c.JupyterHub.proxy_auth_token = 'c33333285d894fffce37e87705e811ecc06f7ad3e9c2c92a62dba7f1f6c7'

#import os
#join = os.path.join
#here = os.path.dirname(__file__)

## ssl config
#ssl = join(here, 'ssl')
#keyfile = join(ssl, 'ssl.key')
#certfile = join(ssl, 'ssl.cert')
#if os.path.exists(keyfile):
#    c.JupyterHub.ssl_key = keyfile
#if os.path.exists(certfile):
#    c.JupyterHub.ssl_cert = certfile




#------------------------------------------------------------------------------
# JupyterHub configuration
#------------------------------------------------------------------------------

# An Application for starting a Multi-User Jupyter Notebook server.

# JupyterHub will inherit config from: Application

# Answer yes to any questions (e.g. confirm overwrite)
# c.JupyterHub.answer_yes = False

# File in which to store the cookie secret.
# c.JupyterHub.cookie_secret_file = 'jupyterhub_cookie_secret'

# Grant admin users permission to access single-user servers.
# 
# Users should be properly informed if this is enabled.
# c.JupyterHub.admin_access = False

# Class for authenticating users.
# 
# This should be a class with the following form:
# 
# - constructor takes one kwarg: `config`, the IPython config object.
# 
# - is a tornado.gen.coroutine
# - returns username on success, None on failure
# - takes two arguments: (handler, data),
#   where `handler` is the calling web.RequestHandler,
#   and `data` is the POST form data from the login page.
# c.JupyterHub.authenticator_class = <class 'jupyterhub.auth.PAMAuthenticator'>

# The date format used by logging formatters for %(asctime)s
# c.JupyterHub.log_datefmt = '%Y-%m-%d %H:%M:%S'

# The cookie secret to use to encrypt cookies.
# 
# Loaded from the JPY_COOKIE_SECRET env variable by default.
# c.JupyterHub.cookie_secret = b''

# 
# c.JupyterHub.tornado_settings = {}

# Interval (in seconds) at which to check if the proxy is running.
# c.JupyterHub.proxy_check_interval = 30

# The port for this process
# c.JupyterHub.hub_port = 8081

# set of usernames of admin users
# 
# If unspecified, only the user that launches the server will be admin.
# c.JupyterHub.admin_users = set()

# The Proxy Auth token.
# 
# Loaded from the CONFIGPROXY_AUTH_TOKEN env variable by default.
#c.JupyterHub.proxy_auth_token = '92f9afe01517dbae810b7cc4f60a04c8f0f38ef1f4acc7d31c6d598c386f'

# The base URL of the entire application
# c.JupyterHub.base_url = '/'

# Path to SSL certificate file for the public facing interface of the proxy
# 
# Use with ssl_key
# c.JupyterHub.ssl_cert = ''

# Set the log level by value or name.
# c.JupyterHub.log_level = 30

# Generate default config file
# c.JupyterHub.generate_config = False

# Include any kwargs to pass to the database connection. See
# sqlalchemy.create_engine for details.
# c.JupyterHub.db_kwargs = {}

# The location of jupyterhub data files (e.g. /usr/local/share/jupyter/hub)
# c.JupyterHub.data_files_path = '/usr/local/share/jupyter/hub'

# Path to SSL key file for the public facing interface of the proxy
# 
# Use with ssl_cert
# c.JupyterHub.ssl_key = ''

# File to write PID Useful for daemonizing jupyterhub.
# c.JupyterHub.pid_file = ''

# Supply extra arguments that will be passed to Jinja environment.
# c.JupyterHub.jinja_environment_options = {}

# The config file to load
# c.JupyterHub.config_file = 'jupyterhub_config.py'

# The port for the proxy API handlers
# c.JupyterHub.proxy_api_port = 0

# The command to start the http proxy.
# 
# Only override if configurable-http-proxy is not on your PATH
# c.JupyterHub.proxy_cmd = 'configurable-http-proxy'

# Interval (in seconds) at which to update last-activity timestamps.
# c.JupyterHub.last_activity_interval = 300

# log all database transactions. This has A LOT of output
# c.JupyterHub.debug_db = False

# The ip for the proxy API handlers
# c.JupyterHub.proxy_api_ip = 'localhost'

# The class to use for spawning single-user servers.
# 
# Should be a subclass of Spawner.
# c.JupyterHub.spawner_class = <class 'jupyterhub.spawner.LocalProcessSpawner'>

# The ip for this process
# c.JupyterHub.hub_ip = 'localhost'

# The public facing port of the proxy
# c.JupyterHub.port = 8000

# Purge and reset the database.
# c.JupyterHub.reset_db = False

# The Logging format template
# c.JupyterHub.log_format = '[%(name)s]%(highlevel)s %(message)s'

# The public facing ip of the proxy
# c.JupyterHub.ip = ''

# The prefix for the hub server. Must not be '/'
# c.JupyterHub.hub_prefix = '/hub/'

# url for the database. e.g. `sqlite:///jupyterhub.sqlite`
# c.JupyterHub.db_url = 'sqlite:///jupyterhub.sqlite'

#------------------------------------------------------------------------------
# Spawner configuration
#------------------------------------------------------------------------------

# Base class for spawning single-user notebook servers.
# 
# Subclass this, and override the following methods:
# 
# - load_state - get_state - start - stop - poll

# Enable debug-logging of the single-user server
# c.Spawner.debug = False

# Timeout (in seconds) before giving up on the spawner.
# 
# This is the timeout for start to return, not the timeout for the server to
# respond. Callers of spawner.start will assume that startup has failed if it
# takes longer than this. start should return when the server process is started
# and its location is known.
# c.Spawner.start_timeout = 60

# The command used for starting notebooks.
# c.Spawner.cmd = ['jupyterhub-singleuser']

# Whitelist of environment variables for the subprocess to inherit
# c.Spawner.env_keep = ['PATH', 'PYTHONPATH', 'CONDA_ROOT', 'CONDA_DEFAULT_ENV', 'VIRTUAL_ENV', 'LANG', 'LC_ALL']

# The notebook directory for the single-user server
# 
# `~` will be expanded to the user's home directory
# c.Spawner.notebook_dir = ''

# Interval (in seconds) on which to poll the spawner.
# c.Spawner.poll_interval = 30

#------------------------------------------------------------------------------
# LocalProcessSpawner configuration
#------------------------------------------------------------------------------

# A Spawner that just uses Popen to start local processes.

# LocalProcessSpawner will inherit config from: Spawner

# Enable debug-logging of the single-user server
# c.LocalProcessSpawner.debug = False

# Timeout (in seconds) before giving up on the spawner.
# 
# This is the timeout for start to return, not the timeout for the server to
# respond. Callers of spawner.start will assume that startup has failed if it
# takes longer than this. start should return when the server process is started
# and its location is known.
# c.LocalProcessSpawner.start_timeout = 60

# Whitelist of environment variables for the subprocess to inherit
# c.LocalProcessSpawner.env_keep = ['PATH', 'PYTHONPATH', 'CONDA_ROOT', 'CONDA_DEFAULT_ENV', 'VIRTUAL_ENV', 'LANG', 'LC_ALL']

# Seconds to wait for process to halt after SIGTERM before proceeding to SIGKILL
# c.LocalProcessSpawner.TERM_TIMEOUT = 5

# The notebook directory for the single-user server
# 
# `~` will be expanded to the user's home directory
# c.LocalProcessSpawner.notebook_dir = ''

# The command used for starting notebooks.
# c.LocalProcessSpawner.cmd = ['jupyterhub-singleuser']

# Seconds to wait for process to halt after SIGINT before proceeding to SIGTERM
# c.LocalProcessSpawner.INTERRUPT_TIMEOUT = 10

# Interval (in seconds) on which to poll the spawner.
# c.LocalProcessSpawner.poll_interval = 30

# Seconds to wait for process to halt after SIGKILL before giving up
# c.LocalProcessSpawner.KILL_TIMEOUT = 5

#------------------------------------------------------------------------------
# Authenticator configuration
#------------------------------------------------------------------------------

# A class for authentication.
# 
# The API is one method, `authenticate`, a tornado gen.coroutine.

# Username whitelist.
# 
# Use this to restrict which users can login. If empty, allow any user to
# attempt login.
c.Authenticator.whitelist = set()

#------------------------------------------------------------------------------
# PAMAuthenticator configuration
#------------------------------------------------------------------------------

# Authenticate local *ix users with PAM

# PAMAuthenticator will inherit config from: LocalAuthenticator, Authenticator

# If a user is added that doesn't exist on the system, should I try to create
# the system user?
# c.PAMAuthenticator.create_system_users = False

# The PAM service to use for authentication.
# c.PAMAuthenticator.service = 'login'

# The encoding to use for PAM
# c.PAMAuthenticator.encoding = 'utf8'

# Username whitelist.
# 
# Use this to restrict which users can login. If empty, allow any user to
# attempt login.
# c.PAMAuthenticator.whitelist = set()
