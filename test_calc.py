import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_addition(self):
        result = calc.addition(2, 3)
        self.assertEqual(calc.addition(2, 3), 5)
        self.assertEqual(calc.addition(2, -3), -1)
        self.assertEqual(calc.addition(-2, -3), -5)
