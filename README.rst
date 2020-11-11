django-random-queryset |Build status|
=====================================

Pull random records using Django ORM.


Requirements
------------

- Python 2.7, 3.6, 3.7
- Django 1.11, 2.0, 2.1, 2.2.


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
        

**No database migrations are needed.**


How to use it:

.. code:: python

    queryset = Model.objects.filter(field=value)
    queryset.random()   # to get one random record
    queryset.random(5)  # to pass limited random records
    queryset.random(len(queryset)) # to get all random records
    queryset.random().values()  # to have access to other queryset methods 


.. |Build status| image:: https://travis-ci.com/rremizov/django-random-queryset.svg?branch=master
   :target: https://travis-ci.com/rremizov/django-random-queryset
