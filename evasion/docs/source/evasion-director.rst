==================
Evasion Director
==================

.. contents::


Introduction
=============

The director takes care of running all the process and parts of the
evasion project. It will run the broker, agency and viewpoint as well 
as any other user defined processes. A typical user process could be 
a web application server, which provides the content for viewpoint to
display. 

The director will check each part is running and will restart if one
part exits.


Director Command Line
======================

The director current provides the current command line options


Director Configuration
=======================

The following is an example configuration as generated using the --create
command line option.


Director API
=============

The python evasion-director provides the `director` package. It provides 
the following functionality.

.. automodule:: evasion.director

