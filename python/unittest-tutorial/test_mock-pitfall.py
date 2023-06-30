import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock
from unittest.mock import patch


class Target(object):
    def apply(self, value):
        return value
    # Let's modify the 'apply' method to take more parameters.
    # Re-run your test and you'll find that it still passes.
    # That's because it isn't built againt your actual API.
    # This is why you should always use the create_autospec method and the autospec parameter with the @patch and @patch.object decorators.
    # def apply(self, value, are_you_sure):
    #     if are_you_sure:
    #         return value
    #     else:
    #         return None


def method(target, value):
    return target.apply(value)


class MethodTestCase(unittest.TestCase):

    def test_method(self):
        target = Mock()

        method(target, "value")

        target.apply.assert_called_with("value")

    # Mocking the method with 'autospec' flag.
    @patch.object(Target, 'apply', autospec=True)
    def test_method_against_actual_api(self, mock_apply):
        target = Target()

        method(target, "value")

        mock_apply.assert_called_with(target, "value")
        target.apply.assert_called_with(target, "value")


if __name__ == '__main__':
    unittest.main()
