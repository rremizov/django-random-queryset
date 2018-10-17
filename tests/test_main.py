import pytest

from .models import ModelA


@pytest.fixture()
def set_up():
    ModelA.objects.bulk_create(ModelA() for _ in range(1000))


@pytest.mark.usefixtures('set_up')
@pytest.mark.django_db
def test_random():
    assert ModelA.objects.random(5).count() == 5
    assert ModelA.objects.random(1001).count() == 1000


@pytest.mark.usefixtures('set_up')
@pytest.mark.django_db
def test_empty_table():
    ModelA.objects.all().delete()
    ModelA.objects.random(1)


@pytest.mark.usefixtures('set_up')
@pytest.mark.django_db
def test_table_with_holes():
    ModelA.objects.random(800).delete()
    assert ModelA.objects.random(50).count() == 50
    assert ModelA.objects.random(500).count() == 200


@pytest.mark.usefixtures('set_up')
@pytest.mark.django_db
def test_filter_random():
    ModelA.objects.filter().random()
