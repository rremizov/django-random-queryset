# encoding: utf-8
import random

from django.db import models



class RandomQuerySet(models.query.QuerySet):

    def random(self, amount=1):
        if amount < 1:
            raise ValueError("'amount' is a positive integer value")

        available_ids = list(self.values_list('id', flat=True))
        selected_ids = set()

        while len(available_ids) and len(selected_ids) < amount:
            model_id = random.choice(available_ids)

            available_ids.remove(model_id)
            selected_ids.add(model_id)

        return self.filter(id__in=selected_ids)

