# encoding: utf-8

import django
from django.db import models

from . import queryset


class RandomManager(models.Manager):
    def random(self, *args, **kwargs):
        return self.get_queryset().random(*args, **kwargs)

    def get_queryset(self):
        return queryset.RandomQuerySet(self.model)
