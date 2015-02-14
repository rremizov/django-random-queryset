# encoding: utf-8

import random


def strategy0(self, amount, available_ids):
    if amount < 1:
        raise ValueError("'amount' is a positive integer value")

    available_ids = list(available_ids)
    selected_ids = set()

    while len(available_ids) and len(selected_ids) < amount:
        selected_id = random.choice(available_ids)

        available_ids.remove(selected_id)
        selected_ids.add(selected_id)

    return selected_ids


DEFAULT = strategy0

