"""
Sample test.
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test calc module"""
    def test_add_numbers(self):
        x = 4
        y = 3
        ans = calc.add(x, y)
        self.assertEqual(ans, 7)

    def test_subtract_numbers(self):
        res = calc.subtract(10, 15)
        self.assertEqual(res, -5)
