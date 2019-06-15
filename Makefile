format:
	isort --recursive django_random_queryset
	isort --recursive tests
	black django_random_queryset
	black tests

test:
	tox --skip-missing-interpreters

develop:
	python setup.py develop

build:
	python setup.py sdist

upload:
	python setup.py sdist upload
