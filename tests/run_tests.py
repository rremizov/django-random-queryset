#!/usr/bin/env python

from __future__ import print_function

import os
import sys

import nose


def run_all(argv=None):
    sys.exitfunc = lambda: sys.stderr.write('Shutting down....\n')

    if argv is None:
        argv = [
            'nosetests',
            '--with-coverage',
            '--cover-package=django_random_query',
            '--cover-erase',
            '--verbose',
        ]

    nose.run_exit(
        argv=argv,
        defaultTest=os.path.abspath(os.path.dirname(__file__))
    )


if __name__ == '__main__':
    run_all(sys.argv)

