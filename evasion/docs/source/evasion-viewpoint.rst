==================
Evasion Viewpoint
==================


Introduction
=============

The viewpoint is a XUL_ application which is run on the latest Firefox_ or GRE_ (Gecko Runtime
Environment). This allows your web application to use the very latest features of HTML5, CSS3
and Javascript. This viewpoint also provides a single browser type to develop for. This means
no hack are needed to support other browsers. If Firefox_ supports it, you can use it!

The Evasion viewpoint is generally a reference implementation and companies to to branch it 
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
If the clicks do not occur with the 20 second window they will be ignored.

To disable this feature hide the status bar.


Command line
------------

To run the evasion-viewpoint in development mode there are two ways of running it. The easiest 
it to use Firefox_


On windows under cmd.exe:
~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: bash

    rem Change to the viewpoint directory:
    rem
    "c:\Program Files\Mozilla Firefox\firefox.exe" -app lib\viewpoint\application.ini

    
On Linux in the shell:
~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: bash

    # Use the system installed firefox to run the Viewpoint
    #
    firefox -app application.ini


Command Line Options
--------------------

-startport <TCP port on localhost>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the port on which the special browser communications can be done. Two viewpoint
instances cannot share the same TCP port. Each needs to operate on its own port.

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



    
.. _GRE: https://developer.mozilla.org/en/gre
.. _Firefox: http://www.mozilla-europe.org/en/firefox/    
.. _XUL: https://developer.mozilla.org/en/xul    
.. _ActiveMQ: http://activemq.apache.org/
.. _RabbitMQ: http://www.rabbitmq.com/
.. _MorbidQ: http://www.morbidq.com/
.. _STOMP: http://stomp.codehaus.org/Protocol
.. _Python: http://www.python.org/

 
 