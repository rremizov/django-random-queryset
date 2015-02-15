# encoding: utf-8

import django
from django.db import models

from . import queryset, strategies


class RandomManager(models.Manager):

    def __init__(self, *args, **kwargs):

        try:
            self._strategy = kwargs.pop('strategy')

        except KeyError:
            self._strategy = strategies.DEFAULT

        super(RandomManager, self).__init__(*args, **kwargs)

    def __getattr__(self, attr, *args):
        try:
            return getattr(self.__class__, attr, *args)
        except AttributeError:
            return getattr(self.__get_queryset(), attr, *args)

    def __get_queryset(self):
        return queryset.RandomQuerySet(self.model, strategy=self._strategy)

    if django.VERSION[1] >= 7:
        get_queryset = __get_queryset

    else:
        get_query_set = __get_queryset

