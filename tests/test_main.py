from django.test import TestCase

from .models import ModelA


class TestMain(TestCase):

    def setUp(self):
        ModelA.objects.bulk_create(ModelA() for _ in range(1000))

    def test_random(self):
        self.assertEqual(ModelA.objects.random(5).count(), 5)
        self.assertEqual(ModelA.objects.random(1001).count(), 1000)

    def test_empty_table(self):
        ModelA.objects.all().delete()
        ModelA.objects.random(1)

    def test_table_with_holes(self):
        ModelA.objects.random(800).delete()
        self.assertEqual(ModelA.objects.random(50).count(), 50)
        self.assertEqual(ModelA.objects.random(500).count(), 200)

    def test_filter_random(self):
        ModelA.objects.filter().random()
