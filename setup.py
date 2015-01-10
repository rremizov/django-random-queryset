from setuptools import setup
import os


def _parse_requirements(filename):
    result = set()
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'requirements',
        filename)

    for line in open(path):
        line = line.strip()

        if not line:
            continue

        if line.startswith('-r'):
            result = result.union(_parse_requirements(line.split(' ')[1]))

        else:
            result.add(line)

    return result


setup(
    name='django-random-queryset',
    version='0.0.1',
    author='Roman M. Remizov',
    author_email='rremizov@yandex.ru',

    license='MIT',
    platforms=('any', ),
    description='',
    long_description=open('README.md').read(),
    url='http://github.com/rremizov/django-random-queryset',

    packages=(
        'django-random-queryset',
    ),
    install_requires=_parse_requirements('pypi.txt'),

    classifiers=(
        'Development Status :: 1 - Planning',
        # 'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.6',
        # 'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',

        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),

    # include_package_data=True,
)

