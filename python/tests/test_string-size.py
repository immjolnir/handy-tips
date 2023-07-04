import unittest
import sys

# string
# cpython/Include/cpython/bytesobject.h
# cpython/Objects/bytesobject.c: PyBytes_FromString, PyBytes_FromObject


class StringSizeTestCase(unittest.TestCase):
    """
    See https://stackoverflow.com/questions/16797459/how-is-str-implemented-in-python
    See http://www.laurentluce.com/posts/python-string-objects-implementation/

    At the C level, Python 3.0 will rename the existing 8-bit string type, called :c:type:`PyStringObject` in Python 2.x, to :c:type:`PyBytesObject`.
    See https://github.com/python/cpython/blob/main/Doc/whatsnew/2.6.rst#pep-3112-byte-literals
    """

    def test_string_sizeof(self):
        self.assertEqual(49, sys.getsizeof(""))
        self.assertEqual(50, sys.getsizeof("t"))
        self.assertEqual(53, sys.getsizeof("test"))


if __name__ == "__main__":
    unittest.main()
