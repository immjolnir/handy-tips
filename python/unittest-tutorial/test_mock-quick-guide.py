import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock


class ProductionClass:
    """
    """
    pass


class ProductionClassTestCase(unittest.TestCase):

    def test_mock_case(self):
        thing = ProductionClass()
        thing.method = MagicMock(return_value=3)
        thing.method(3, 4, 5, key='value')

        thing.method.assert_called_with(3, 4, 5, key='value')


#
# mock = Mock(side_effect=KeyError('foo'))
# mock()
#
# values = {'a': 1, 'b': 2, 'c': 3}
# def side_effect(arg):
#    return values[arg]
#
# mock.side_effect = side_effect
# mock('a'), mock('b'), mock('c')
#
# mock.side_effect = [5, 4, 3, 2, 1]
# mock(), mock(), mock()
#
if __name__ == '__main__':
    unittest.main()
