import uuid

from django.db import models

from django_random_queryset import managers, strategies


class ModelA(models.Model):
    uuid = models.CharField(default=lambda: str(uuid.uuid4()), max_length=128)

    objects = managers.RandomManager()
    index_selection = managers.RandomManager(strategy=strategies.index_selection)
    index_exclusion = managers.RandomManager(strategy=strategies.index_exclusion)
    index_combo = managers.RandomManager(strategy=strategies.index_combo)

    def __str__(self):
        return self.uuid

