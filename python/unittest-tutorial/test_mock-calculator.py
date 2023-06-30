import unittest
from unittest import TestCase
from unittest.mock import patch

from calculator import Calculator
from calculator import SleepyCalculator


class TestCalculator(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        answer = self.calc.sum(2, 4)
        self.assertEqual(answer, 6)


class TestSleepyCalculator(TestCase):
    def setUp(self):
        self.calc = SleepyCalculator()

    @unittest.skip("It costs too much time.")
    def test_sum_sum_with_sleep(self):
        """
        It is clearly not a good idea to call the sum method as is every time we run tests.
        This is a situation where we can use mocking to speed up our tests and avoid an undesired effect at the same time.
        """
        answer = self.calc.sum(2, 4)
        self.assertEqual(answer, 6)

    @patch("calculator.SleepyCalculator.sum", return_value=9)
    def test_sum(self, sum):
        """
        It replaces the actual sum function with a mock function that behaves exactly how we want.
        In this case, our mock function always returns 9.
        During the lifetime of our test, the sum function is replaced with its mock version.

        While this may seem counter-intuitive at first, remember that mocking allows you to provide a so-called fake implementation of the part of your system you are testing. This gives you a lot of flexibility during testing.
        """
        self.assertEqual(sum(2, 4), 9)


if __name__ == '__main__':
    unittest.main()
