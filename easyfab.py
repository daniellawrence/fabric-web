#!/usr/bin/env python
from fabric import main
import settings

def get_fab_tasks():
    fab_task_list = {}

    if type(settings.fabfile).__name__ == 'dict':
        for alias, fabfile in settings.fabfile.items():
            (docstring, tasks, default) = main.load_fabfile(fabfile)
            fab_task_list[alias] = {'tasks': tasks,
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
        hosts[hostname].append( message )

    return hosts
