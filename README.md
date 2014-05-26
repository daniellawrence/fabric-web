fabric-web
==========

Taking the magic of fabric and throwing up as a website for ease of use

How to install
-----------------

Quick install onto your local machine.

    $ git clone https://github.com/daniellawrence/fabric-web
    $ pip install -r requirements.txt
	

How to run
------------

This will start the server on <http://localhost:5000/>

    $ ./main.py

screenshots
-------------

Selecting a task from one of the imported fabfile.py's
![index][index]

Add the required fields and choose the host(s) to run it on
![task][task]

Review the results
![results][results]

Just Added
------------

Horrible hacks to pull apart per-task decorators for hosts and roles.


settings
--------

Where to look for main fabfile that should be imported.
 
````python
fabfile = {
 'fabric-web': './fabfile.py'
 'users': './fabfile-users.py'
 'packages': './fabfile-packages.py'
}
````


[index]: https://raw.github.com/daniellawrence/fabric-web/master/screenshots/index.png "Index"
[task]: https://raw.github.com/daniellawrence/fabric-web/master/screenshots/run_task.png "Run task.png"
[results]: https://raw.github.com/daniellawrence/fabric-web/master/screenshots/results.png "results"
Mon Apr  8 22:18:07 EST 2013
