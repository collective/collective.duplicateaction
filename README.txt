collective.duplicateaction
===========================

This package adds new content action "Duplicate" into the "Actions" menu next to standard actions like "Copy", "Cut", "Paste", "Rename" and "Delete".

This does not aim to be as general as possible but it may speed things up.


Installing
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This package requires Plone 3.x or later (tested on 4.1).

Installing without buildout
------------------------------

Install this package in either your system path packages or in the lib/python
directory of your Zope instance. You can do this using either easy_install or
via the setup.py script.

Installing with buildout
------------------------------

If you are using `buildout`_ to manage your instance installing
collective.duplicateaction is even simpler. You can install
collective.duplicateaction by adding it to the eggs line for your instance::

    [instance]
    eggs = collective.duplicateaction

After updating the configuration you need to run the ''bin/buildout'', which
will take care of updating your system.

.. _buildout: http://pypi.python.org/pypi/zc.buildout


How it works
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. New action "Duplicate" is installed into the "Actions" content menu

2. Duplicate action as available only if user is allowed to add current content type into its parent folder and if has permissions to copy or move content

3. When user clicks the action link it copies current content, pastes its copy into parent folder and redirects user to the new duplicated content


Copyright and Credits
~~~~~~~~~~~~~~~~~~~~~~~~~~~

collective.deactivateaction is licensed under the GPL. See LICENSE.txt for details.


Author: `Lukas Zdych (lzdych)`__

.. _lzdych: mailto:lukas.zdych@gmail.com

__ lzdych_

