"""
Sample tests
"""

from django.test import SimpleTestCase

from . import calc


class ClacTest(SimpleTestCase):
    """Test the calc module."""
    def test_add_numbers(self):
        """Test adding number together."""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        """Test subtracting numbers."""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
