""" Taking the magic of fabric and throwing up as a website for ease of use.
"""
#!/usr/bin/env python
from flask import Flask
from flask import render_template
from flask import request, redirect, flash
#
from fabric import state
import easyfab

import settings

app = Flask(__name__)
task_list = easyfab.get_fab_tasks()

def render(template, *args, **kwargs):
    """ render a template with a set of standard args that every template
    can take advantage of.
    This stops every call to render_template adding in the same extra **kwargs
    """
    return render_template(template, state=state, env=state.env, 
            settings=settings, *args, **kwargs)

def get_task(fabfile, task_name):
    """ Given a fabfile and task_name, return the task object. """
    return task_list[fabfile]['tasks'][task_name]

@app.route("/")
def index():
    """ Basic landing page, with a list of all the tasks from all the fabfiles.
    """
    return render('index.html', task_list=task_list)

@app.route("/fabfile/<fabfile>")
def task_display_single_Fabfile(fabfile):
    """ Provide a fabfile to list only the tasks from that fabfile. """
    local_task_list = task_list.copy()
    for fabfile_name in local_task_list.keys():
        if fabfile_name == fabfile:
            continue
        del local_task_list[fabfile_name]
    return render('index.html', task_list=local_task_list)

@app.route("/fabfile/<fabfile>/task/<task_name>/")
def task_display(fabfile, task_name):
    task = get_task(fabfile, task_name)
    single_wrapped_task = task.__dict__['wrapped']
    import inspect
    argspec = inspect.getargspec( single_wrapped_task )
    source_code = inspect.getsource(single_wrapped_task)
    task_dict = task.__dict__
    task_dict['argspec'] = argspec
    task_dict['source_code'] = source_code

    args = argspec.args
    defaults = argspec.defaults

    if defaults:
        number_of_defaults = len(defaults) * -1
        args_with_defaults = zip( args[number_of_defaults:], defaults)
        args_without_defaults = args[:number_of_defaults]
    else:
        args_with_defaults = []
        args_without_defaults = args


    return render('task_form.html', task=task, 
                wrapped_task=single_wrapped_task, 
                task_dict=task_dict,
                args_with_defaults=args_with_defaults, 
                args_without_defaults=args_without_defaults
                )

def execute_task(task, hosts, roles, *args, **kwargs):
    """ Execute a task, providing all the details from the form. """
    from fabric.api import env, execute
    from StringIO import StringIO
    import sys

    env.hosts = hosts
    env.roles = roles

    output = StringIO()
    error = StringIO()
    sys.stdout = output
    sys.stderr = error

    data = None
    try:
        data = execute(task, *args, **kwargs)
    except SystemExit:
        print "fabric had a fatal exception, that caused it to exit."
    finally:
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

    print "data: %s" % data
    print "out: %s" % str(output.getvalue())
    print "err: %s" % str(error.getvalue())

    return output.getvalue(), error.getvalue()

@app.route("/settings/apply", methods=['POST'])
def fabric_settings_apply():
    """ Apply the settings from the settings form. """
    return render('settings.html')

@app.route("/settings")
def fabric_settings():
    """ Offer a html form for tuning application settings. """
    return render('settings.html')

@app.route("/fabfile/<fabfile>/task/<task_name>/execute", methods=['POST'])
def task_execute(fabfile, task_name):
    """ Read in the form post, then execute the task. """
    task = get_task(fabfile, task_name)
    form = request.form.copy()

    hosts = form['env_hosts'] + ' '
    roles = request.form['env_roles'] + ' '
    del form['env_hosts']
    del form['env_roles']

    if ',' in hosts:
        hosts = hosts.split(',')

    if ' ' in hosts:
        hosts = hosts.split()

    if ',' in roles:
        roles = roles.split(',')

    if ' ' in roles:
        roles = roles.split()

    if not hosts and not roles:
        flash('You need to provide either a hostname or choose a role.')
        return redirect("/fabfile/%(fabfile)s/task/%(task_name)s" % locals())

    stdout, stderr = execute_task(task, hosts=hosts, roles=roles, **form)

    stdout = easyfab.format_output(stdout)

    return render('execute.html', task=task, results=stdout, errors=stderr)
    


if __name__ == '__main__':
    app.host       = settings.listen_ip
    app.port       = settings.listen_port
    app.debug      = settings.debug
    app.secret_key = settings.secret_key
    app.run()
