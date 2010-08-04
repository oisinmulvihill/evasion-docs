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

Project Creation
----------------

paster create --template=evasion.web-project


App Creation
------------

paster create --template=evasion.web-app



RunWeb Command
==============

runweb is the command used to run the 



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



