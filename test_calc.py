import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calc.addition(2, 3), 5)
        self.assertEqual(calc.addition(2, -3), -1)
        self.assertEqual(calc.addition(-2, -3), -5)

    def test_subtraction(self):
        self.assertEqual(calc.subtraction(4, 3), 1)
        self.assertEqual(calc.subtraction(2, 3), -1)
        self.assertEqual(calc.subtraction(2, -3), 5)
        self.assertEqual(calc.subtraction(-2, -3), 1)

    def test_multiplication(self):
        self.assertEqual(calc.multiplication(2, 3), 6)
        self.assertEqual(calc.multiplication(2, -3), -6)
        self.assertEqual(calc.multiplication(-2, -3), 6)
        self.assertEqual(calc.multiplication(0, -3), 0)

    def test_division(self):
        """ 正常系 """
        self.assertEqual(calc.division(5, 2), 2.5)
        self.assertEqual(calc.division(5, -2), -2.5)
        self.assertEqual(calc.division(6, 2), 3)
        self.assertEqual(calc.division(9, -3), -3)
        self.assertEqual(calc.division(0, 2), 0)

        """ 異常系 """
        with self.assertRaises(ValueError):
            calc.division(5, 0)
