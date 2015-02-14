# encoding: utf-8

import random

from django.db import models

from django_random_queryset import strategies



class RandomQuerySet(models.query.QuerySet):

    def __init__(self, strategy=strategies.DEFAULT, *args, **kwargs):
        self._strategy = strategy

        super(RandomQuerySet, self).__init__(*args, **kwargs)

    def random(self, amount=1):
        return self.filter(id__in=self._strategy(
            amount,
            self.values_list('id', flat=True)))

