import pytest

from handypy import division

@pytest.mark.skip("ZeroDivisionError")
def test_division():
    res = division.divide(1, 0)

def test_division_with_exception_handler():
    res = division.divide_with_exception_handler(1, 0)
