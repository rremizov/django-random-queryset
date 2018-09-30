#!/usr/bin/env python

import os
import shutil

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'


import django
from django.core.management import call_command
django.setup()

try:
    shutil.rmtree('tests/migrations', True)
    call_command('makemigrations', 'tests')
    call_command('test', 'tests')
finally:
    shutil.rmtree('tests/migrations', True)