===============
Evasion Agency
===============

.. contents::


Introduction
=============

The Agency take care of loading and managing the "agents". The configuration
determines what agents are loaded at run time.


The Agency
===========
  
This is the agency that manages the physical hardware and 
abstracts its use from the other parts of the code.

The agency catagorises the hardware under a generic set
of classifications defined in AGENT_CATEGORIES. This is then used 
to provide a generic id when the need arises to directly address 
a agent. The ids follow a path type syntax. The root of all is 
the 'agent' node. Agents are then hung off the root node based
on the class they belong to. For example::

  /agent/printer
  /agent/display
  /agent/swipe
  /agent/sale
  :
  etc

Once a specifc agent is registered for use in the configuration
then it gets added and aliased. For example a configuration entry
for the magtek usb swipe could be::

  [magtekusb]
  # required agent manager config
  #
  alias = '1' # optional, auto-set if not provided.
  cat = 'swipe'
  agent = 'magtek.usbcardswipe.swipe'
  
  # specific config
  vendor_id = 0x0801
  product_id = 0x0002

This instructs the agency's manager to create a agent::

  /agent/swipe/magtekusb/1

  /agent/swipe/1

The agent manager loads the agent package 'magtek.usb.swipe' from the
python path. The agency looks from a Base class in the module. In the 
magtek example this would be 'magtek.usb.swipe.Base'. This class 
implements the required interface the manager uses to control the agent. 


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



Agency Module
=============

.. automodule:: evasion.agency

