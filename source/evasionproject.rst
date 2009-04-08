================
Evasion Project 
================


:author: Oisin Mulvihill, Folding Software Limited.


Introduction
=============

Evasion project is a framework to allow web applications to escape the bounds in which
they are normally bound. It allows you application to access hardware and react in real
time to events...

deviceaccess
============


messenger
=========


Viewpoint
=========

Dependancies
------------

XulRunner: 
 * https://developer.mozilla.org/en/XULRunner

PyXPCOM:
 * https://developer.mozilla.org/en/PyXPCOM

This is how the pyxpcom and xulrunner initial viewpoint app was constructed:
 * http://pyxpcomext.mozdev.org/no_wrap/tutorials/pyxulrunner/python_xulrunner_setup.html

For more information on creating a simple XULRunner app, have a look at the myapp.zip sample from:
 * https://developer.mozilla.org/en/Getting_started_with_XULRunner


Development Set up
------------------

MacOSX
~~~~~~

From the project root you need to run "viewpoint_mac_devsetup.sh". This creates a the absolute path
symlink from the "viewpoint" to "Resources" inside the "platform/macosx/viewpoint.app/Contents"
To release the project the contents of the viewpoint resources could be copied instead. 

Windows
~~~~~~~

I'm not sure yet how to get this to work as symlinks don't work here...


