"""
Example on how to use tests for TDD
"""
from django.test import TestCase

from .models import I4pProfile

class TestExample(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_something(self):
        """
        That must start with test_
        """
        pass
        





