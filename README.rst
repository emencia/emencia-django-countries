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
  ...   'emencia.django.countries',
  ... )

Now you can run a *syncdb* for installing the models into your database and the list of all country contained in a fixture.


Usage
=====

By default when the fixture is loaded all the countries a leveled to 0, 
the default and displayed by alphabetical order. ::

  >>> from emencia.django.countries.models import Country
  >>> Country.objects.all()
  [<Country: Afghanistan>, <Country: Albania>, <Country: Algeria>, '...(remaining elements truncated)...']

So if you don't want to display *Afghanistan* as the first country of your list, 
you have a set a high value to the **level** attribute for all the countries you want.

Now if you want to retrieve your country list ordered do this : ::

  >>> france = Country.objects.get(iso='FR')
  >>> france.level = 100
  >>> france.save()

  >>> Country.objects.all()
  [<Country: France>, <Country: Afghanistan>, <Country: Albania>, '...(remaining elements truncated)...']

But if you only want a short list of countries with the level attribute set, you can do this : ::

  >>> Country.objects.leveled()
  [<Country: France>]

This will return only the countries with a level value different than 0.

Template Context Processors
===========================

Sometimes it can be usefull to have all the countries in the context for rendering templates,
so a template context processor is provided. ::

  >>> TEMPLATE_CONTEXT_PROCESSORS = (
  ...      # Your template context processors
  ...      'emencia.django.countries.context_processors.countries',
  ...	)

This template context processor, provides 2 variables in the context :

  * COUNTRIES_LIST
  * COUNTRIES_LIST_LEVELED

Template tags
=============

But in general it's a waste of ressources to have all the countries loaded in the context,
because it make a database request for each request, so template tags have been implemented.

In your templates, to get the countries list, simply do this. ::

  {% load countries_tags %}

  {% get_countries %}

It will load the countries list in the local context of the template, in a variable named **COUNTRIES**
But if you want to change the name of this variable use this syntax. ::

  {% get_countries as MY_COUNTRIES %}

If you only want to have the short list of countries, use this tag. ::

  {% get_countries_leveled as MY_COUNTRIES %}

Of course the same syntax apply to this tag.

