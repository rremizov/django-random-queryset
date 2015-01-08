from django.test import TestCase

from .models import ModelA


class TestMain(TestCase):
    fixtures = ['basic']

    def test_main(self):
        self.assertEqual(ModelA.objects.random(5).count(), 5)
        self.assertEqual(ModelA.objects.random(25).count(), 20)

