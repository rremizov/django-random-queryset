import os

from setuptools import setup


def _parse_requirements(filename):
    result = list()
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'requirements',
        filename)

    for line in open(path):
        line = line.strip()

        if not line:
            continue

        if line.startswith('-r'):
            result.extend(_parse_requirements(line.split(' ')[1]))
        else:
            result.append(line)

    return result


setup(
    name='django-random-queryset',
    version='0.0.4',
    author='Roman M. Remizov',
    author_email='rremizov@yandex.ru',

    license='MIT',
    platforms=['any'],
    description="The extension gives you ability to pull random records using Django's ORM.",
    long_description=open('README.rst').read(),
    url='http://github.com/rremizov/django-random-queryset',

    packages=[
        'django_random_queryset',
    ],
    install_requires=_parse_requirements('base.txt'),

    test_suite='tests.run_tests.run_all',
    tests_require=_parse_requirements('test.txt'),

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
