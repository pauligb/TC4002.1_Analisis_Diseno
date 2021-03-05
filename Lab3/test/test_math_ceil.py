import unittest
import math

# Boundary from Right-BICEP is considered in the test cases
# Inverse relationship from Right-BICEP is considered in the test cases
# Error conditions from Right-BICEP is considered in the test cases by using assertions

class TestMathCeil(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(math.ceil(101.96), 102)

    def test_almost_zero(self):
        self.assertEqual(math.ceil(0.1), 1)
        self.assertEqual(math.ceil(-0.1), 0)

    def test_is_zero(self):
        self.assertEqual(math.ceil(0.0), 0)

    def test_negative_number(self):
        self.assertEqual(math.ceil(-13.1), -13)
