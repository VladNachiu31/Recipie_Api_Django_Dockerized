"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calcul


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calcul.add(5, 6)

        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        """Test subtracting numbers."""
        res = calcul.subtract(10, 15)

        self.assertEqual(res, 5)
