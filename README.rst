.. _Django: https://www.djangoproject.com/

========================
Emencia Django Countries
========================

A Django application who contains world country list that can be displayed with a priority order.

Usefull for forms or for models which needs a country list ordered.

.. contents::

Links
*****

* Download his `PyPi package <https://pypi.python.org/pypi/emencia.django.countries>`_;
* Clone it on his `repository <https://github.com/emencia/emencia-django-countries>`_;

Requires
********

* ``setuptools``;
* `Django`_ >= 1.4 (should be compatible to *Django 1.8* and beyond);

Install
*******

First install the package: ::

    pip install emencia.django.countries

Add it to your installed Django apps in settings:

.. sourcecode:: python

    INSTALLED_APPS = (
        ...
        'emencia.django.countries',
        ...
    )
    
Finally run the Django commands ``migrate`` to install app database tables, this will also fill ``Country`` model with initial datas for countries.

Usage
*****

By default when the fixture is loaded all the countries a leveled to 0, 
the default and displayed by alphabetical order.

.. sourcecode:: python

    >>> from emencia.django.countries.models import Country
    >>> Country.objects.all()
    [<Country: Afghanistan>, <Country: Albania>, <Country: Algeria>, '...(remaining elements truncated)...']

So if you don't want to display *Afghanistan* as the first country of your list, 
you have a set a high value to the **level** attribute for all the countries you want.

Now if you want to retrieve your country list ordered do this:

.. sourcecode:: python

    >>> france = Country.objects.get(iso='FR')
    >>> france.level = 100
    >>> france.save()

    >>> Country.objects.all()
    [<Country: France>, <Country: Afghanistan>, <Country: Albania>, '...(remaining elements truncated)...']

But if you only want a short list of countries with the level attribute set, you can do this:

.. sourcecode:: python

    >>> Country.objects.leveled()
    [<Country: France>]

This will return only the countries with a level value different than 0.

Template Context Processors
---------------------------

Sometimes it can be usefull to have all the countries in the context for rendering templates,
so a template context processor is provided.

.. sourcecode:: python

    >>> TEMPLATE_CONTEXT_PROCESSORS = (
    ...      # Your template context processors
    ...      'emencia.django.countries.context_processors.countries',
    ... )

This template context processor, provides 2 variables in the context :

* COUNTRIES_LIST
* COUNTRIES_LIST_LEVELED

Template tags
-------------

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

