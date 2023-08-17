from setuptools import setup

setup(
    name="django-random-queryset",
    version="0.1.3",
    author="Roman Remizov",
    author_email="rremizov@yandex.ru",
    license="MIT",
    platforms=["any"],
    description="Pull random records using Django ORM.",
    long_description=open("README.rst").read(),
    url="http://github.com/rremizov/django-random-queryset",
    packages=["django_random_queryset"],
    install_requires=["django>=1.11.27"],
    test_suite="tests.run_tests.run_all",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
