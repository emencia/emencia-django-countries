========================
Emencia Django Countries
========================

Emencia.django.countries is a Django application who contains world country list, who can be displayed with a priority order.

Usefull for forms or for models which needs a country list ordered.

.. contents::

Installation
============

You could retrieve the last sources from http://github.com/Fantomas42/emencia-django-countries and running the installation script ::
    
  $> python setup.py install

or use pip ::

  $> pip install -e git://github.com/Fantomas42/emencia-django-countries.git#egg=emencia.django.countries


In your projects
================

Register **emencia.django.countries** in your INSTALLED_APPS section your project settings. ::

  >>> INSTALLED_APPS = (
  ...   # Your favorites apps
  ...   'emencia.django.countries',)

Now you can run a *syncdb* for installing the models into your database and the list of all country contained in a fixture.


Usage
=====

By default when the fixture is loaded all the countries a leveled to 0, 
the default and displayed by alphabetical order.

So if you don't want to display *Afghanistan* as the first country of your list, 
you have a set a high value to the **level** attribute for all the countries you want.

Now if you want to retrieve your country list ordered do this : ::

  >>> from emencia.django.countries.models import Country
  >>> Country.objects.all()
  ... [<Country: Afghanistan>, <Country: Albania>, <Country: Algeria>, '...(remaining elements truncated)...']

  >>> france = Country.objects.get(iso='FR')
  >>> france.level = 100
  >>> france.save()
  >>> Country.objects.all()
  ... [<Country: France>, <Country: Afghanistan>, <Country: Albania>, '...(remaining elements truncated)...']

But if you only want a short list of countries with the level attribute set, you can do this : ::

  >>> Country.objects.leveled()
  ... [<Country: France>]

This will return only the countries with a level value different than 0.


