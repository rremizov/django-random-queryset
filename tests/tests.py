from django.test import TestCase

from .models import ModelA


class TestMain(TestCase):
    fixtures = ['basic']

    def test_brute_force(self):
        self.assertEqual(ModelA.brute_force.random(5).count(), 5)
        self.assertEqual(ModelA.brute_force.random(25).count(), 20)

    def test_index_selection(self):
        self.assertEqual(ModelA.index_selection.random(5).count(), 5)
        self.assertEqual(ModelA.index_selection.random(25).count(), 20)

    def test_index_exclusion(self):
        self.assertEqual(ModelA.index_exclusion.random(5).count(), 5)
        self.assertEqual(ModelA.index_exclusion.random(25).count(), 20)

    def test_index_combo(self):
        self.assertEqual(ModelA.index_combo.random(5).count(), 5)
        self.assertEqual(ModelA.index_combo.random(25).count(), 20)

