==================
Evasion Viewpoint
==================


Introduction
=============

The viewpoint is a XUL_ application which is run on the latest Firefox_ or GRE_ (Gecko Runtime
Environment). This allows your web application to use the very latest features of HTML5, CSS3
and Javascript. This viewpoint also provides a single browser type to develop for. This means
no CSS hacks are needed to support other browsers. If Firefox_ supports it you can use it!

The Evasion viewpoint is generally a reference implementation and companies generally branch it 
and implement their own versions. This allows you to customise the start or screen or further
refine the interface.


Running the Viewpoint
=====================

Knocking Feature
----------------

This allows the Viewpoint to be flipped between two URIs changing between 'normal' and 
'admin' mode. When the status bar on the Viewpoint is clicked more the 7 times within 
20 seconds, the Viewpoint will toggle between admin and normal modes. In admin mode the
-adminuri or its default it loaded. In normal mode -starturi or its default is loaded.
If the clicks do not occur within the 20 seconds they will be ignored.

To disable this feature hide the status bar.


Via the Director
----------------

The Viewpoint has two modes of operation under the director kiosk and passive mode. You
can copy either configuration sections into the director configuration.


Passive Mode
~~~~~~~~~~~~

In "Passive Mode" no Viewpoint process is started. If one is detected on the control port
it is directedto the start URI, when the URI becomes available. If the URI does not respond 
then the URI will not be loaded.

This mode is used in applications where the director is running as a service on windows or 
under init on linux. 


.. sourcecode:: ini

    [viewpoint]
    # Standard options example:
    disabled = 'no'
    order = 1
    controller = 'evasion.director.controllers.viewpointpassive'

    # The URI to connect to when the URI is present and the viewpoint
    # is ready to recieve requests. The viewpoint will also be kept
    # looking at this URI so it can't navigate away out of the app.
    uri = "http://myhost:myport/myapp"        
    
    # The method to use to check that web application is ready
    # for requests:
    #
    # The default method is 'connect' which just checks a socket
    # connection to the URI will succeed.
    #
    # The alternative method is 'recover' which will try a
    # HEAD or GET method on the URI.
    #
    test_method = 'connect'

    # This is the control port which will be listened on for
    # command requests on. 7055 is the default if not given.
    port = '7055'


Kiosk Mode
~~~~~~~~~~

In "Kiosk Mode" the Viewpoint is run as a process and actively restarted if it exits. When
it is started it is directed at URI given in the configuration, when that URI becomes available.
If the URI does not respond then the initial URI will not be changed.

This mode is used in applications that typically should not exit and will always be running.

.. sourcecode:: ini

    [viewpoint]
    # Standard options example:
    disabled = 'no'
    order = 9
    controller = 'evasion.director.controllers.viewpoint'
    
    # Specific configuration:
    #
    # The URI to connect to when the URI is present and the viewpoint
    # is ready to recieve requests. The viewpoint will also be kept
    # looking at this URI so it can't navigate away out of the app.
    uri = "http://myhost:myport/myapp"        
    
    # The admin uri which is allowed. If this isn't set then the
    # viewpoint will repoint at the 'uri'
    admin_uri = "http://myhost:myport/myapp"        
    
    # The method to use to check that web application is ready
    # for requests:
    #
    # The default method is 'connect' which just checks a socket
    # connection to the URI will succeed.
    #
    # The alternative method is 'recover' which will try a
    # HEAD or GET method on the URI. This can also be set to
    # 'disable' to prevent checking and redirection.
    #
    test_method = 'connect'

    # This is the control port which will be listened on for
    # command requests on. 7055 is the default if not given.
    port = '7055'

    # The xulrunner exe to use (command and/or path to exe):
    xulrunner = 'xulrunner'
    
    # Director to run the xul application from:
    workingdir = '.'

    # Example command line args you could use:
    #
    # -starturi chrome://viewpoint/content/static/startup.html
    #    The URI to display on start up. By default it uses
    #    its internal evasion viewpoint page.
    #
    # -nofullscreen no | yes
    #    Disable the full screen mode. The default is to run
    #    in full screen mode.
    #
    # -development no | yes
    #    Show an address bar and a reload button to aid in
    #    development of an application.
    # :
    # :
    # etc
    #
    args = ''


From the command line
---------------------

To run the evasion-viewpoint in development mode there are two ways of running it. The easiest 
it to use Firefox_


On windows under cmd.exe:
~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: bash

    rem Change to the viewpoint directory:
    rem
    "c:\Program Files\Mozilla Firefox\firefox.exe"  -app evasion\viewpoint\application.ini

    
On Linux in the shell:
~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: bash

    # Use the system installed firefox to run the Viewpoint
    #
    firefox -app evasion/viewpoint/application.ini


Command Line Options
--------------------

-startport <TCP port on localhost>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the port on which the XUL Control Protocol communications take place. Two 
viewpoint instances cannot share the same TCP port. Each needs to operate on its own port.

The default port is 7055.


-starturi <URI>
~~~~~~~~~~~~~~~

This is the page to load when the Viewpoint starts. This provides the URI that the 
"Knocking Feature" will direct to in normal mode.

The default points at the internal start up page using the chrome URI 
'chrome://viewpoint/content/static/startup.html'

-adminuri <URI>
~~~~~~~~~~~~~~~

This provides the URI that the "Knocking Feature" will direct to in admin mode.

The default uri is 'http://127.0.0.1:28909/'


-nofullscreen <no | yes>
~~~~~~~~~~~~~~~~~~~~~~~~

If this is 'no' the Viewpoint will take up the whole screen. This is a way to maximise
the Viewpoint at start up for touch screen applications.

The default is 'yes'.


-development <no | yes>
~~~~~~~~~~~~~~~~~~~~~~~

This provides an 'address bar' for development debugging purposes. It provides a simple
reload, go and address URI entry.

The default is 'no'.


-width <number>
~~~~~~~~~~~~~~~

This is the default width that is used when the Viewpoint is not running in fullscreen mode.

The default is '1024'.


-height <number>
~~~~~~~~~~~~~~~~

This is the default height that is used when the Viewpoint is not running in fullscreen mode.

The default is '768'.


-hidestatus <yes | no>
~~~~~~~~~~~~~~~~~~~~~~

This removes the default status bar which shows the loading message. If this is removed the
"knock" feature will no be available.

The default is 'no'.


Development
===========

Control from Python_
--------------------

There are two programtic ways of controlling the Viewpoint from Python_. The first is via
direct socket communication. The second is via the messaging system. 

Direct Control
~~~~~~~~~~~~~~

This is the easiest to use and is based around the following code. The Viewpoint will need
to be running, although it doesn't need to be running as part of the director.

..sourcecode:: python

  # TODO: code parse include docs here:
  evasion.director.viewpointdirect.DirectBrowserCalls

The director provide a command line tool called viewpointdirect which can be used as a 
refenerence implementation for this approach.

The main disadvantage of this approach is that remote system cannot communicate with the
Viewpoint run on a machine. It only binds to localhost. The messaging system is the 
alternative way of controlling the Viewpoint. This can be called remotely.


Message based Control
~~~~~~~~~~~~~~~~~~~~~

This is a bit more involved to set up but not needlessly so. The director needs to be running 
and configured. The Viewpoint configuration should be in either Passive or Kiosk mode. 

Next your program needs to be running as part of the messaging system. For more details on this
see the evasion.messenger documentation. Assuming your program is then you can now use the 
following code. 

This class wraps the messenging specifics and provides a nice programatic way to use the Viewpoint
signals.

..sourcecode:: python

  # TODO: code parse include docs here:
  evasion.director.viewpointcontrol.BrowserCalls


viewpointdirect
---------------

The evasion.director provides a command line tool which can be used to execute any of the 
XUL Control Protocol commands.

.. sourcecode:: bash

    # Linux/Mac
    viewpointdirect
    
    # Windows
    viewpointdirect.exe

It has the following command line options:
    
.. sourcecode:: bash

    $ viewpointdirect -h
    Usage: viewpointdirect [options]

    Options:
      -h, --help            show this help message and exit
      -c CMD, --command=CMD
                            Command to use. Default: get_uri
      -a ARGS, --args=ARGS  The comm port the browser is using. Default: Nothing
      -p PORT, --port=PORT  The comm port the browser is using. Default: 7055
      -i HOST, --host=HOST  The comm interface the browser is listening on.
                            Default: 127.0.0.1

        
Example: loading a new page
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: bash

    viewpointdirect -c set_uri -a http://www.google.com
    
    2010-08-04 17:54:10,328 evasion.director.viewpointdirect.main INFO Running command 'set_uri' with args 'http://www.google.com'.
    2010-08-04 17:54:10,328 evasion.director.viewpointdirect.DirectBrowserCalls DEBUG setBrowserUri: Sending command: {"replyto": "no-one", "data": {"args": {"uri": "http://www.google.com"}, "command": "set_uri"}}
    2010-08-04 17:54:10,358 evasion.director.viewpointdirect.DirectBrowserCalls DEBUG setBrowserUri: rc {"result":"ok", "data":"http://www.google.com", "replyto":"no-one"}


XUL Control Protocol
--------------------

The XUL Control Protocol implements a series of commands that can be used to control the Viewpoint. 
This control is completely separate from the site that may be loaded into the browser. The commands 
can occur at any stage. 

Normally the [wiki:Messenger] takes care of the physical socket connection and data shifting. However 
the higher level command dictionary, called the control frame, must be set up correctly by the user.

Control Frame
~~~~~~~~~~~~~

The control frame is a python dictionary that is converted to JSON. It must contain only data 
and types that are supported by simplejson_ and the JSON_ specification. By virtue of the fact 
that the actual control object sent to the browser is in JSON, means that control is not 
limited to just Python_. Any language that can generate this structure could also be used to 
control the Viewpoint.

The control frame has the general format:

.. sourcecode:: python

    control_frame = {
        'command' : '..valid command string..',
        'args' : {..keyword arguments..}
    }


Response
~~~~~~~~

Once a command frame has been sent to the Viewpoint then a reponse object is returned. This 
object has been encode via JSON and when loaded will convert into the python dictionary. The 
reponse has the general 

format:

.. sourcecode:: python

    response = {
        'result' : '.. ok or fail..',
        'data' : '.. returned data or error message ..'
    }


XUL Control Commands
--------------------

The javascript file evasion/viewpoint/chrome/content/outbandcontrol.js implements the physical 
server side socket handling. The main point of interest in this file is 
obc.inputReceived.success(...) method. This converts the received data structure from JSON into 
a native javascript object. This function also wraps the onward command calls and catches any 
exceptions, which are returned as errors to the caller. This function also takes care of the 
'replyto' field that is used by the Messenger for replying to waiting callers.

The actual function implementations are in evasion/viewpoint/chrome/content/xulcontrolhandler.js. 
The xch.process(command, args) function takes care of mapping the commands to javascript calls. 
This function also handles the error exception for unknown commands. To add new functionality this 
is where you start.


Error Handling
~~~~~~~~~~~~~~

If a command fail for whatever reason the response['result'] will contain the 'error'. The capture 
exception or error message will then be present in response['data'].


replace
~~~~~~~

This command replaces the DOM element in the loaded page with the given HTML content instead.

If I have the following page loaded in the browser:

.. sourcecode:: html

    <html xmlns="http://www.w3.org/1999/xhtml">

      <head>
        <meta content="text/html; charset=UTF-8" http-equiv="content-type" py:replace="''"/>
            <title>${page_title} - ${tg.site_wide.company_name}</title>
      </head>

      <body>
        <div id="main">
            <h1>Hello there!</h1>
            <p>
                This is some test content in the body of the document.<br/>
                <br/>
                <div id="toplevel"/>
                <br/>
            </p>
        </div>
      </body>
    </html>

I could replace the empty toplevel div as follows:

.. sourcecode:: python

    replacement = """
    <div id='toplevel'>
        <h3>Extra Content</h3>
        <p>
            This is some extra I've just put into the DOM tree.
        </p>
    </div>
    """

    control_frame = {
        'command' : 'replace',
        'args' : {'id':'toplevel', 'content':replacement}
    }
    
    resp = browser.run(control_frame)
    assert resp['result'], 'ok'

If the browser was able to replace the DOM element then the result will be 'ok' otherwise 'fail' 
and the error message will be returned.


exit
~~~~

This command instructs the Viewpoint to exit. This command is special as it does not return a 
reponse. It will close the control connection and perform an ordered shutdown of the application.

The control frame for this command is:

.. sourcecode:: python

    control_frame = {
        'command' : 'exit',
        'args' : {}
    }

    response = None


version
~~~~~~~

This returns the XUL Control Protocol version string.

The control frame for this command is:

.. sourcecode:: python

    control_frame = {
        'command' : 'version',
        'args' : {''}
    }

The usual response is a confirmation of the uri that has been sent:

.. sourcecode:: python

    response = {
        'result' : 'ok',
        'data' : 'XUL Control Protocol vX.Y.Z YYYY-MM-DD'
    }


set_uri
~~~~~~~

This tells the browser to load the given uri.

The control frame for this command is:

.. sourcecode:: python

    control_frame = {
        'command' : 'set_uri',
        'args' : {'uri' : 'http://..some.site.dot.whatever../'}
    }

The usual response is a confirmation of the uri that has been sent:

.. sourcecode:: python

    response = {
        'result' : 'ok',
        'data' : 'http://..some.site.dot.whatever../'
    }

    
get_uri
~~~~~~~

This returns the URI that the browser is currently looking at.

The control frame for this command is:

.. sourcecode:: python

    control_frame = {
        'command' : 'get_uri',
        'args' : {}
    }

The usual response is a confirmation of the uri that has been sent:

.. sourcecode:: python

    response = {
        'result' : 'ok',
        'data' : 'http://..the.url.thats.loaded../'
    }
    

Useful
======

XulRunner
---------
 
For more information on creating a simple XULRunner app, have a look at the myapp.zip sample from:

* https://developer.mozilla.org/en/Getting_started_with_XULRunner

General XUL Runner information:

* https://developer.mozilla.org/en/XULRunner
 
 
PyXPCOM:
---------

Not used, however its possible to use Python instead of javascript to create a XUL app. The downside
though is it increases the overhead as you need an extension in the XUL app you might generate.

* https://developer.mozilla.org/en/PyXPCOM


















.. _JSON: http://json.org/
.. _simplejson: http://cheeseshop.python.org/pypi/simplejson
.. _GRE: https://developer.mozilla.org/en/gre
.. _Firefox: http://www.mozilla-europe.org/en/firefox/    
.. _XUL: https://developer.mozilla.org/en/xul    
.. _ActiveMQ: http://activemq.apache.org/
.. _RabbitMQ: http://www.rabbitmq.com/
.. _MorbidQ: http://www.morbidq.com/
.. _STOMP: http://stomp.codehaus.org/Protocol
.. _Python: http://www.python.org/

 
 