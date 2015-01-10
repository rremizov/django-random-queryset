import uuid

from django.db import models

from django_random_queryset.managers import RandomManager


class ModelA(models.Model):
    uuid = models.CharField(default=lambda: str(uuid.uuid4()), max_length=128)

    objects = RandomManager()

    def __str__(self):
        return self.uuid

