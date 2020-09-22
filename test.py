import unittest
from main import *
import math


class MyTestCase(unittest.TestCase):
    def test_sqrt_normal(self):
        self.assertAlmostEqual(sqrt(0.25), 0.5)
        self.assertAlmostEqual(sqrt(4), 2)
        self.assertAlmostEqual(sqrt(13), math.sqrt(13))
        self.assertEqual(sqrt(-0.25), -1)

    def test_sqrt_type(self):
        self.assertRaises(BaseException, sqrt("gf"))

    def test_sqrt_break_rec(self):
        self.assertRaises(BaseException, sqrt(5785923047))

    def test_power_normal(self):
        self.assertEqual(power(1, 10), 1)
        self.assertEqual(power(123, -5), -1)
        self.assertEqual(power(12, 2.5), 144)
        self.assertEqual(power(0.5, 2), 0.25)

    def test_power_type(self):
        self.assertRaises(BaseException, power(12, "two"))
        self.assertRaises(BaseException, power("one", 13))


if __name__ == '__main__':
    unittest.main()
