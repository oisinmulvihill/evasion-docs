===========
Evasion Web
===========


.. contents::


Introduction
=============

The "evasion.web" is a customised version of the Pylons_ web framework. It allows a web application
to be made out of "Apps". Each "App" could provide all of the web application or specific parts. Each
App is a special Python_ package. They can derive from each other and so can allow highly reuseable
functionality to be developed.

"evasion.web" can be used on its own and is not dependant on the other parts. It could also be
potentially be replaced with other web framework such as Django_, Flask_, etc. You could
even decide to use static files and javascript to generate the interface.


Quickstart
==========

You

Development
===========

Introduction
------------

The Evasion Web breaks a "Web Project" into two sections. The first is
the project and the second is the "app" packages.

The project at its minimum contains the configuration which lists in order the
app packages to load. The "runweb" command is then used with this to run the
"Web Project".

Each "app" can deliver a part of functionality. You could have a single app
package which does the entire Web Project. The value of splitting a large project
into smaller parts, is the ability to reuse "apps" in other projects.


Project Creation
----------------

To create a top-level "Web Project" you call paster to create a project for
you::

    paster create -t evasion.web-project FancyProject


App Creation
------------

To create an "App" which the web project can use call paster as follows::

    paster create -t evasion.web-app Part1


RunWeb Command
==============

Change into Part1 app and do a "python setup.py develop". This will put Part1
package into the python PATH. Change into the FancyProject and edit the
"development.ini".  On line 51::

  web_modules =

Add the Part1 app::

  # The package name will be in lower case:
  web_modules = part1

Save and exit the editor. Now start the Web Project using the runweb command::

    # Go with the default 'development.ini'
    runweb

    # Or specifying the configuration:
    runweb --config=development.ini

    $runweb
    options.config_filename:  development.ini
    2011-08-21 18:21:46,841 evasion.web.scripts.runweb.Run DEBUG init: config dir:'/home/oisin/src/EvasionWeb/evasion-web/evasion/web/scripts'
    2011-08-21 18:21:46,841 evasion.web.scripts.runweb.Run DEBUG init: self.iniFile:'/home/oisin/src/EvasionWeb/FancyProject/development.ini'
    Running webapp.
    2011-08-21 18:21:46,844 evasion.web.scripts.runweb.Run INFO main: running mainloop (no messenger).
    2011-08-21 18:21:46,844 evasion.web.config.environment INFO load_environment: enabling default middleware (enable_default_middleware = true).
    2011-08-21 18:21:46,844 evasion.web.config.environment WARNING load_environment: default auth middleware disabled (enable_default_auth = false).
    2011-08-21 18:21:46,848 evasion.web.config.environment INFO load_environment: director evasion.web modules '['part1']'.
    2011-08-21 18:21:46,848 evasion.web.config.environment INFO load_environment: loading module 'part1'.
    2011-08-21 18:21:46,851 evasion.web.config.environment DEBUG load_environment: appending middleware to list: <function custom_middleware_handler at 0x914e6f4>
    2011-08-21 18:21:46,851 evasion.web.config.environment DEBUG load_environment: appending to setup app list: <function setup_app at 0x914e764>
    2011-08-21 18:21:46,852 evasion.web.config.environment DEBUG load_environment: configure() returned:
    {'controllers': '/home/oisin/src/EvasionWeb/Part1/lib/part1/controllers',
     'desc': '',
     'g': <part1.Handy object at 0x9153aec>,
     'kind': 'web',
     'map': <routes.mapper.Mapper object at 0x9155cac>,
     'middleware': <function custom_middleware_handler at 0x914e6f4>,
     'model': None,
     'modelmanager': None,
     'name': 'part1',
     'setup_app': <function setup_app at 0x914e764>,
     'static': '/home/oisin/src/EvasionWeb/Part1/lib/part1/static',
     'templates': '/home/oisin/src/EvasionWeb/Part1/lib/part1/templates'}

    2011-08-21 18:21:46,857 evasion.web.config.middleware DEBUG Calling middleware '<function default_middleware at 0x914e25c>' -
    2011-08-21 18:21:46,884 evasion.web.config.middleware DEBUG Calling middleware '<function custom_middleware_handler at 0x914e6f4>' -
    Example custom_middleware_handler for 'part1'.
    2011-08-21 18:21:46,884 evasion.web.config.middleware INFO load_environment: enabling default error handling middleware (enable_default_errorhandling = true).
    2011-08-21 18:21:46,884 evasion.web.scripts.runweb.Run INFO appmain: Serving webapp
    serving on http://127.0.0.1:6080


You can now open "http://127.0.0.1:6080" in a web browser.


Code Documentation
==================

.. automodule:: evasion.web







.. _GRE: https://developer.mozilla.org/en/gre
.. _Firefox: http://www.mozilla-europe.org/en/firefox/
.. _XUL: https://developer.mozilla.org/en/xul
.. _PythonPro:     http://#
.. _pydispatcher: http://pydispatcher.sourceforge.net/
.. _ActiveMQ: http://activemq.apache.org/
.. _RabbitMQ: http://www.rabbitmq.com/
.. _MorbidQ: http://www.morbidq.com/
.. _STOMP: http://stomp.codehaus.org/Protocol
.. _Python: http://www.python.org/
.. _Pylons: http://pylonshq.com/
.. _Flask: http://flask.pocoo.org/
.. _Django: http://www.djangoproject.com
.. _NewmanOnline: http://www.newmanonline.org.uk
