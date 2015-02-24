"""
Custom Authenticator to use to for HBP workshop JupyterHub

"""
import json
import os

from tornado import gen

from jupyterhub.handlers import BaseHandler
from jupyterhub.auth import Authenticator, LocalAuthenticator
from jupyterhub.utils import url_path_join

from IPython.utils.traitlets import Unicode


class TextAuthenticator(Authenticator):
    """Class for authentication where user names and passwords are taken from a text file"""
    
    passwdfile= Unicode('users.txt', config=True)
    
    def check_passwd(self, user, passwd):
        """Checks username and password from the file"""
        f = open( self.passwdfile, 'r')
        lines = [line.split() for line in f  if line.split() and line.split()[0] == user]
        if not lines:
            self.log.warn('could not find user %s', user )
            return False
        if len lines > 1 :
            self.log('user %s with more than one line in passwd file', user)
        #here it will take the last line only 
        return passwd == lines[-1][1]
            
    @gen.coroutine
    def authenticate(self, handler, data):
        user = data['username']
        passwd = data['password']
        if self.check_passwd(user, passwd):
            return user

