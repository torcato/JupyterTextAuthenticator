import pytest
from .. import rawauthenticator

test = rawauthenticator.TextAuthenticator()


def test_auth():
    passwdfile = 'users.txt'
    f = open(passwdfile, 'w')
    f.write('cesar\t123\n')
    f.write('angela\t456\n')
    f.close()
    auth = rawauthenticator.TextAuthenticator()
    auth.passwdfile = passwdfile
    
    assert auth.check_passwd('cesar', '123') == True
    assert auth.check_passwd('angela', '456') == True
    assert auth.check_passwd('cesar', '456') == False

#def test_auth(io_loop):
#    passwdfile = 'users.txt'
#    f = open(passwdfile, 'w')
#    f.write('cesar\t123\n')
#    f.write('angela\t456\n')
#    f.close()
#    
#    authenticator = rawauthenticator.TextAuthenticator()
#    auth.passwdfile = passwdfile
#    authorized = io_loop.run_sync(lambda : authenticator.authenticate(None, {
#        'username': 'cesar',
#        'password': '123',
#    }))
#    assert authorized == 'cesar'
#    
#    authorized = io_loop.run_sync(lambda : authenticator.authenticate(None, {
#        'username': 'cesar',
#        'password': '456',
#    }))
#    assert authorized is None

#    authorized = io_loop.run_sync(lambda : authenticator.authenticate(None, {
#        'username': 'angela',
#        'password': '456',
#    }))
#    assert authorized == 'angela'

