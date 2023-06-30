import unittest


class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Without using a subtest, execution would stop after the first failure, and the error would be less easy to diagnose because the value of i wouldn’t be displayed:
        """
        for i in range(0, 6):
            self.assertEqual(i % 2, 0)


class NumbersTest_with_subTest(unittest.TestCase):
    """
    When there are very small differences among your tests, for instance some parameters, unittest allows you to distinguish them inside the body of a test method using the subTest() context manager.

    """

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)


if __name__ == '__main__':
    unittest.main()
