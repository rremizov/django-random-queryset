# encoding: utf-8

import django
from django.db import models

from . import queryset


class RandomManager(models.Manager):

    def __getattr__(self, attr, *args):
        try:
            return getattr(self.__class__, attr, *args)
        except AttributeError:
            return getattr(self.__get_queryset(), attr, *args)

    def __get_queryset(self):
        return queryset.RandomQuerySet(self.model)

    if django.VERSION[1] >= 7:
        get_queryset = __get_queryset
    else:
        get_query_set = __get_queryset
