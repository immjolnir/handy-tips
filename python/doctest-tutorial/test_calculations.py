# test_calculations.py
# see https://realpython.com/python-doctest/

import doctest
import unittest

# The load_tests() function is automatically called by unittest, and the framework discovers tests in your code.
# tests.addTests(...) loads the doctest tests defined in test_calculations.txt and converts them into a unittest test suite.
def load_tests(loader, tests, ignore):
    # The highlighted line does the magic:
    tests.addTests(doctest.DocFileSuite("test_calculations.txt"))

    # If your doctest tests live in your code's docstring, then you can integrate them into your unittest suites:
    import calculations
    tests.addTests(doctest.DocTestSuite(calculations))
    return tests

# Your unittest tests goes here...

if __name__ == "__main__":
    unittest.main()

