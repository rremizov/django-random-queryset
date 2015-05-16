django-random-queryset |Build status|
======================

The extension gives you ability to pull random records using Django's ORM.


Requirements
------------

Python 2.7 or 3.2, Django 1.5+.


Installation
------------

.. code:: sh

    $ pip install django-random-queryset


Setup
-----


Add ``RandomManager`` to desired model:

.. code:: python

    from django.db import models

    from django_random_queryset import RandomManager


    class Model(models.Model):

        objects = RandomManager()

        # ...


Use it:

.. code:: python

    queryset = Model.objects.filter(field=value)
    queryset.random()   # to get one random record
    queryset.random(5)  # pass amount to get more records
    queryset.random().values()  # other queryset methods available


.. |Build status| image:: https://travis-ci.org/rremizov/django-random-queryset.svg?branch=master
   :target: https://travis-ci.org/Suor/django-cacheops

