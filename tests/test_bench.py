import pytest

from .models import ModelA


@pytest.mark.parametrize('table_size', [1000, 10000, 100000])
@pytest.mark.parametrize('random_size', [1, 10, 100, 1000])
@pytest.mark.django_db
def test_bench(benchmark, table_size, random_size):
    ModelA.objects.bulk_create(ModelA() for _ in range(table_size))
    benchmark(ModelA.objects.random, random_size)
