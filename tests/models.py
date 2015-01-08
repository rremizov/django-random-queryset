import uuid

from django.db import models

from django_random_queryset import RandomManager


class ModelA(models.Model):
    uuid = models.CharField(default=ModelA.default_uuid, max_length=128)

    objects = RandomManager()

    @classmethod
    def default_uuid(cls):
        return str(uuid.uuid4())

    def __str__(self):
        return self.attr0

