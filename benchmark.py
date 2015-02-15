#!/usr/bin/env python
# encoding: utf-8

import json
import logging
import timeit


class Test:

    def __init__(self, amount, strategy_name):
        self._amount = amount
        self._strategy_name = strategy_name
        self._list = repr(list(range(10000)))
        self._result = None

    def run(self):
        statement = '{}({}, {})'.format(
            self._strategy_name, self._amount, self._list)
        setup = 'from django_random_queryset.strategies import {}'.format(
            self._strategy_name)

        self._result = timeit.timeit(statement, setup=setup, number=100)

    def result(self):
        return dict(
            strategy=self._strategy_name,
            amount=self._amount,
            time=self._result)


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(
        '%(asctime)s;%(name)s;%(levelname)s;%(message)s'))
    logger.addHandler(handler)

    return logger


def drange(start, stop, step):
    current = start

    while current < stop:
        yield current
        current += step


def main():

    logger = get_logger()

    tests = list()
    tests.extend([
        Test(i, 'brute_force')
        for i in drange(1, 2500, 100)
    ])
    tests.extend([
        Test(i, 'index_selection')
        for i in drange(1, 10000, 100)
    ])
    tests.extend([
        Test(i, 'index_exclusion')
        for i in drange(1, 10000, 100)
    ])
    tests.extend([
        Test(i, 'index_combo')
        for i in drange(1, 10000, 100)
    ])

    for no, test in enumerate(tests):
        test.run()
        logger.info('{}/{}'.format(no, len(tests)))

    results = [test.result() for test in tests]

    with open('results.json', 'w') as fh:
        json.dump(dict(results=results), fh, indent=4)


if __name__ == '__main__':
    main()

