#!/usr/bin/env python
""" This is a demo fabfile that has been include to show you that the docstring
in the fabfile file is what is shown here.
This can be handy to give the user an overview of tasks, that are located within
this fabfile.
"""

from fabric.api import task, run, settings, hide
from fabric.api import env
from fabric.decorators import hosts, roles

env.roledefs = {
    'web': ['www1', 'www2', 'www3'],
    'dns': ['ns1', 'ns2']
}

@task
def uname(arg1, hostname='localhost', username='root'):
    """ my2 fab2 file2. """
    with settings(hide('everything')):
        run('uname -a')
    run('uname -a')

@task
def get_remote_kernel():
    """ Connect to a remote system to gather its kernel version. """
    run('uname -r')

@task
def run_command(executable_command):
    """ Connect to the remote system(s) are run any command that you type in. """
    run("%s" % "".join(executable_command))


@roles('web')
@task
def task_with_roles_deco():
    """ This has as a fabric.decorators.roles(*role_list)"""
    run('id')

@hosts('web')
@task
def task_with_hosts_deco():
    """ This has as a fabric.decorators.hosts(*host_list)"""
    run('id')

@hosts('localhost','localhost')
@task
def task_with_2hosts_deco():
    """ This has as a fabric.decorators.hosts(*host_list)"""
    run('id')

@roles('web')
@hosts('localhost')
@task
def task_with_hosts_and_roles_deco():
    """ This has as a fabric.decorators.hosts(*host_list) and fabric.decorators.roles(*role_list)"""
    run('id')

