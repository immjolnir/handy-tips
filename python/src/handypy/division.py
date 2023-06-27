import sys

def divide(Dividend, Divisor):
    """
        return Dividend / Divisor
    ZeroDivisionError: division by zero
    """
    return Dividend / Divisor


def divide_with_exception_handler(Dividend, Divisor):
    try:
        return Dividend / Divisor
    except Exception as e:
        print("=" * 20)
        # print(traceback.format_exec())
        print(sys.exc_info())
        print("=" * 20)
