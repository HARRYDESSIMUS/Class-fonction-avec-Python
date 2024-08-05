import unittest

class TestCalculateDiscount(unittest.TestCase):
    def test_15_percent_discount(self):
        result = calculate_discount(100, 0.15)
        self.assertEqual(result, 85.0)  