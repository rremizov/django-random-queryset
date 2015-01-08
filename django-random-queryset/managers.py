# encoding: utf-8

from django.db import models

from .queryset import RandomQuerySet


class RandomManager(models.Manager):

    def __getattr__(self, attr, *args):
        try:
            return getattr(self.__class__, attr, *args)
        except AttributeError:
            return getattr(self.get_query_set(), attr, *args)

    def get_query_set(self):
        return RandomQuerySet(self.model)

