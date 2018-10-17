test:
	DJANGO_SETTINGS_MODULE=tests.settings cosmic-ray init ray.yml .ray-session
	DJANGO_SETTINGS_MODULE=tests.settings cosmic-ray exec .ray-session
	cosmic-ray dump .ray-session | cr-report

develop:
	python setup.py develop

build:
	python setup.py sdist

upload:
	python setup.py sdist upload
