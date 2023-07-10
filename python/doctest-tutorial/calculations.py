# calculations.py
# $ python -m doctest -v calculations.py

def add(a, b):
    """Compute and return the sum of two numbers.

    Usage examples:
    >>> add(4.0, 2.0)
    6.0
    >>> add(4, 2)
    6.0
    """
    return float(a + b)

def divide(a, b):
    """Compute and return the quotient of two numbers.

    Usage examples:
    >>> divide(84, 2)
    42.0
    >>> divide(15, 3)
    5.0
    >>> divide(42, -2)
    -21.0

    >>> divide(42, 0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
    """
    # The first highlighted line holds a header that’s common to all exception tracebacks. The second highlighted line contains the actual exception and its specific message. These two lines are the only requirement for doctest to successfully check for expected exceptions.
    return float(a / b)

