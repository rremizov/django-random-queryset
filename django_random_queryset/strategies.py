# encoding: utf-8
from __future__ import division

import math
import random


class SmallPopulationSize(Exception):
    pass


def min_max(sample_size, min_id, max_id, rows_count):
    assert (max_id - min_id) + 1 == rows_count
    population = list(range(min_id, max_id + 1))
    return random.sample(population, sample_size)


def min_max_count(desired_sample_size, min_id, max_id, rows_count):
    assert (max_id - min_id) + 1 >= rows_count, "{}, {}, {}".format(
        min_id, max_id, rows_count
    )
    id_holes_amount = (max_id - min_id) + 1 - rows_count
    id_holes_ratio = id_holes_amount / (max_id - min_id)
    assert 0 <= id_holes_ratio <= 1

    population = list(range(min_id, max_id + 1))
    actual_sample_size = int(
        math.ceil(desired_sample_size * max(1, math.ceil(1 / id_holes_ratio)))
    )
    actual_sample_size *= 10

    if actual_sample_size >= rows_count or actual_sample_size > len(population):
        raise SmallPopulationSize()

    return random.sample(population, actual_sample_size)
