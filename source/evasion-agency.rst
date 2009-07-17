===============
Evasion Agency
===============

.. contents::


Introduction
=============

The Agency take care of loading and managing the "agents". The configuration
determines what agents are loaded at run time.

.. automodule:: agency.agency


Agent
=====

What is an Agent
-----------------

An Agent is an interface to a piece of hardware, network service or any other
item that could possibly be controlled. An Agent defines a set of "signals"
and an API which can be used. When the Agent is then hooked into the messaging 
system, any other part can communicate with this agent. 


The Agent Module
-----------------

An Agent is simply a python module that implements a basic interface. You derive
from the `agency.agent.Base` and the loader system will the use this as an agent
in the running system.



Agency API
==========

.. automodule:: agency.agent
.. automodule:: agency.config
.. automodule:: agency.manager
