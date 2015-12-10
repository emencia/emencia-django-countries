Changelog
=========

Version 0.2.1 - 2015/12/10
--------------------------

* Fixed bad path for ``HISTORY.rst`` in ``setup.py``;

Version 0.2.0 - 2015/12/10
--------------------------

* Ensure compatibility with ``Django>=1.7``:
  
  * Added compatibility support in model manager with ``get_queryset`` method;
  * Added Django migration;
  * Now loading initial data fixtures from a data migration since ``Django>=1.7`` don't do it automatically anymore;

* Update setup.py for better package classifier and packages infos;

Version 0.1.1 - 2013/09/26
--------------------------

* Fix package MANIFEST for missing rule for fixture data file;

Version 0.1 - 2013/05/03
------------------------

* First release as a package;
