# coding=utf-8

import os

SECRET_KEY = "secret_key"

DEFAULT_CHARSET = "utf-8"

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
)

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = ("django.contrib.auth", "django.contrib.contenttypes", "tests")

if os.environ.get("TEST_DATABASE_ENGINE") == "postgresql":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "django_random_queryset",
            "USER": "django_random_queryset",
            "PASSWORD": "password",
            "HOST": "localhost",
            "PORT": "5432",
        }
    }
elif os.environ.get("TEST_DATABASE_ENGINE") == "mysql":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "django_random_queryset",
            "USER": "django_random_queryset",
            "PASSWORD": "",
            "HOST": "",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "sqlite.db",
            # Make in memory sqlite test db to work with threads
            # See https://code.djangoproject.com/ticket/12118
            "TEST": {"NAME": ":memory:cache=shared"},
        }
    }
