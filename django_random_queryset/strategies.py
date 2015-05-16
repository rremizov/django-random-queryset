# encoding: utf-8

import random


def index_selection(amount, available_ids):
    """
    Slow with (amount / len(available_ids)) close to 1.
    """

    if amount < 1:
        raise ValueError("'amount' is a positive integer value")

    available_ids_length = len(available_ids)

    if amount > available_ids_length:
        return available_ids

    selected_indexes = set()

    while len(selected_indexes) < amount:
        selected_indexes.add(random.randint(0, available_ids_length - 1))

    return {available_ids[index] for index in selected_indexes}


def index_exclusion(amount, available_ids):
    """
    For cases with (amount / len(available_ids)) close to 1.
    """

    if amount < 1:
        raise ValueError("'amount' is a positive integer value")

    available_ids_length = len(available_ids)

    if amount > available_ids_length:
        return available_ids

    excluded_indexes = set()
    amount_to_exclude = available_ids_length - amount

    while len(excluded_indexes) < amount_to_exclude:
        excluded_indexes.add(random.randint(0, available_ids_length - 1))

    selected_ids = set(available_ids)

    for index in excluded_indexes:
        selected_ids.remove(available_ids[index])

    return selected_ids


def index_combo(amount, available_ids):

    if not available_ids:
        return set()

    if float(amount) / len(available_ids) < 0.5:
        return index_selection(amount, available_ids)

    else:
        return index_exclusion(amount, available_ids)


DEFAULT = index_combo

