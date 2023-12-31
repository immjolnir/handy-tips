import unittest


class Widget:
    def __init__(self, name, width=50, length=50):
        self._name = name
        self._width = width
        self._length = length

    def size(self):
        return (self._width, self._length)

    def resize(self, width, length):
        self._width = width
        self._length = length


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50, 50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size(), (100, 150),
                         'wrong size after resize')


if __name__ == '__main__':
    unittest.main()
