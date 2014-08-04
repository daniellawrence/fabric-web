# Where to look for main fabfile that should be imported.
# fabfile = {
#   'fabric-web': './fabfile.py'
#   'users': './fabfile-users.py'
#   'packages': './fabfile-packages.py'
#   }
#
fabfile = {'example-fabfile': './fabfile.py'}

# default secert key that is used for flash
# Change this...
secret_key = 'secret_key'

# IP that the fabric-web flask server should listen on
listen_ip = '127.0.0.1'
# PORT that the fabric-web flask server should listen on
listen_port = 5000

# Turn on debug
debug = True

# Show hostname field
show_hostname_field = True

# show task code in execute form
show_task_code_in_execution_form = True

# Grab you local settings, without messing up the git_commit
try:
    import local_settings # flake8: noqa
except ImportError:
    pass
