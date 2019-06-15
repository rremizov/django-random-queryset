import uuid

from django.db import models
from django_random_queryset import managers


class ModelA(models.Model):
    uuid = models.CharField(default=uuid.uuid4, max_length=128)

    objects = managers.RandomManager()

    def __str__(self):
        return self.uuid
