import unittest


class SwapTestCase(unittest.TestCase):
    """There's no built-in function in Python that could be used to swap values of veriablesBut you can simply build it using the swap syntax: 'a, b = b, a'
    See https://blogboard.io/blog/knowledge/python-swap/
    """
    def test_string(self):
        a = "Hello"
        b = "World"
        a, b = b, a
        self.assertEqual("World", a)
        self.assertEqual("Hello", b)

    def test_list(self):
        a = [1, 2, 3, 4]
        b = [5, 6, 7, 8]
        a, b = b, a
        self.assertEqual([5, 6, 7, 8], a)
        self.assertEqual([1, 2, 3, 4], b)

    def test_map(self):
        a = {1:2, 3:4}
        b = {5: 6, 7: 8}
        a, b = b, a
        self.assertEqual({5: 6, 7: 8}, a)
        self.assertEqual({1: 2, 3: 4}, b)


if __name__ == '__main__':
    unittest.main()

