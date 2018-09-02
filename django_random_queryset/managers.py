# encoding: utf-8

import django
from django.db import models

from . import queryset


class RandomManager(models.Manager):

    def random(self, *args, **kwargs):
        return self.__get_queryset().random(*args, **kwargs)

    def __get_queryset(self):
        return queryset.RandomQuerySet(self.model)

    if django.VERSION[1] >= 7:
        get_queryset = __get_queryset
    else:
        get_query_set = __get_queryset
