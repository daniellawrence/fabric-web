# Where to look for main fabfile that should be imported.
# 
# fabfile = {
#   'fabric-web': './fabfile.py'
#   'users': './fabfile-users.py'
#   'packages': './fabfile-packages.py'
#   }
#
fabfile = {'fabric-web': './fabfile.py'}

# default secert key that is used for flash
# Change this...
secret_key = 'secret_key'

# IP that the fabric-web flask server should listen on
listen_ip = '127.0.0.1'
# PORT that the fabric-web flask server should listen on
listen_port = 5000

# Turn on debug
debug = True

# Grab you local settings, without messing up the git_commit
try:
    import local_settings
except ImportError:
    pass
