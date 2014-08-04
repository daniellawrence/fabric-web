#!/usr/bin/env python
from fabric import main
import settings
import inspect


def get_fab_tasks():
    fab_task_list = {}

    if type(settings.fabfile).__name__ == 'dict':
        for alias, fabfile in settings.fabfile.items():
            (docstring, tasks, default) = main.load_fabfile(fabfile)
            fab_task_list[alias] = {
                'tasks': tasks,
                'doc': docstring,
                'default': default,
                'alias': alias,
            }
    return fab_task_list


def format_output(output):
    import re
    import collections
    hosts = collections.defaultdict(list)
    for line in output.split('\n'):
        line = line.strip()
        m = re.match(r'^\[(.*?)\] (.*)', line)
        if not m:
            continue
        (hostname, message) = m.groups()
        hosts[hostname].append(message)

    return hosts


def task_to_dict(task):
    """ Pull apart a task in to an easily consumable dict. """

    task = task.wrapped

    hosts = []
    roles = []

    # Loop over the many decorators until we find the hosts and/or roles
    # This is Horrible
    while 'wrapped' in task.__dict__:
        if 'hosts' in task.__dict__:
            hosts = task.__dict__['hosts']
        if 'roles' in task.__dict__:
            roles = task.__dict__['roles']
        task = task.wrapped

    argspec = inspect.getargspec(task)
    source_code = inspect.getsource(task)
    task_dict = task.__dict__

    args = argspec.args
    defaults = argspec.defaults

    if defaults:
        number_of_defaults = len(defaults) * -1
        args_with_defaults = zip(args[number_of_defaults:], defaults)
        args_without_defaults = args[:number_of_defaults]
    else:
        args_with_defaults = []
        args_without_defaults = args

    task_dict['args_with_defaults'] = args_with_defaults
    task_dict['args_without_defaults'] = args_without_defaults
    task_dict['argspec'] = argspec
    task_dict['source_code'] = source_code
    task_dict['args'] = args
    task_dict['defaults'] = defaults
    task_dict['roles'] = roles
    task_dict['hosts'] = hosts

    return task_dict


