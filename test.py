import unittest
from main import *
import math
from datetime import datetime
import random


class TestCalculator(unittest.TestCase):
    def setUp(self):
        a = random.randint(1, 10000)
        self.calculator = Calculator(a)

    def test_random(self):
        print(datetime.now())
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.add(1, 2, 3).value, calc_value + 6)
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.multiply(5, 2, 90).value, calc_value * 900)
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.divide(2, 3).value, calc_value / 6)
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.divide(2, 3).value, calc_value / 6)
        calc_value = self.calculator.value
        self.assertAlmostEqual(self.calculator.root().value, math.sqrt(calc_value))
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(2).value, math.pow(calc_value, 2))
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.add(1).multiply(9).divide(3).power(2).value, (calc_value+1)*(calc_value+1)*9)

    def test_add(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.add(1, 2, 3).value, calc_value + 6)
        self.assertRaises(BaseException, self.calculator.add("adad"))
        self.calculator.value = "12"
        self.assertRaises(BaseException, self.calculator.add(1))

    def test_add_type(self):
        self.assertRaises(BaseException, self.calculator.add("happy"))
        self.calculator.value = "sad"
        self.assertRaises(BaseException, self.calculator.add(1))

    def test_mul(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.multiply(5, 2, 90).value, calc_value * 900)

    def test_mul_type(self):
        self.assertRaises(BaseException, self.calculator.multiply("happy"))
        self.calculator.value = "sad"
        self.assertRaises(BaseException, self.calculator.multiply(1))

    def test_divide(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.divide(2, 3).value, calc_value / 6)

    def test_divide_type(self):
        self.assertRaises(BaseException, self.calculator.divide("happy"))
        self.calculator.value = "sad"
        self.assertRaises(BaseException, self.calculator.divide(1))

    def test_divide_zero(self):
        self.assertRaises(BaseException, self.calculator.divide(0))

    def test_root_normal(self):
        calc_value = self.calculator.value
        self.assertAlmostEqual(self.calculator.root().value, math.sqrt(calc_value))
        self.calculator.value = 0.25
        self.assertAlmostEqual(self.calculator.root().value, 0.5)
        self.calculator.value = 4
        self.assertAlmostEqual(self.calculator.root().value, 2)
        self.calculator.value = 13
        self.assertAlmostEqual(self.calculator.root().value, math.sqrt(13))
        self.calculator.value = -0.25
        self.assertEqual(self.calculator.root().value, -0.25)

    def test_root_type(self):
        self.calculator.value = "sd"
        self.assertRaises(BaseException, self.calculator.root())

    def test_power_normal(self):
        self.calculator.value = 1
        self.assertEqual(self.calculator.power(10).value, 1)
        self.calculator.value = 2
        self.assertEqual(self.calculator.power(-2).value, 0.25)
        self.calculator.value = 12
        self.assertEqual(self.calculator.power(2.5).value, 144)
        self.calculator.value = 0.5
        self.assertEqual(self.calculator.power(2).value, 0.25)

    def test_power_type(self):
        self.calculator.value = 12
        self.assertRaises(BaseException, self.calculator.power("two"))
        self.calculator.value = "one"
        self.assertRaises(BaseException, self.calculator.power(13))
        print(datetime.now())


if __name__ == '__main__':
    unittest.main()

