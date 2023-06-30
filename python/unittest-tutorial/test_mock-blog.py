import unittest
from unittest import TestCase
from unittest.mock import patch, Mock

import blog


class TestBlog(TestCase):
    def setUp(self):
        self.blog = blog.Blog("TestBlog")

    @unittest.skip("external link not available.")
    def test_blog_posts(self):
        response = self.blog.posts()
        self.assertTrue(response)

    # You can see from the code snippet that the test_blog_posts function is decorated with the @patch decorator.
    # When a function is decorated using @patch, a mock of the class, method or function passed as the target to @patch is returned and passed as an argument to the decorated function.
    # In this case, @patch is called with the target blog.Blog and returns a Mock which is passed to the test function as MockBlog.
    # It is important to note that the target passed to @patch should be importable in the environment @patch is being invoked from. In our case, an import of the form `from blog import Blog` should be resolvable without errors.
    #
    # Note that MockBlog is a variable name to represent the created mock and can be you can name it however you want.
    #
    @patch('blog.Blog')
    def test_blog_posts_mock(self, MockBlog):
        mock_blog = MockBlog("TestBlog with mock")

        mock_blog.posts.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'Test Title',
                'body': 'Far out in the uncharted backwaters of the unfashionable  end  of the  western  spiral  arm  of  the Galaxy\ lies a small unregarded yellow sun.'
            }
        ]

        # Calling blog.posts() on our mock blog object returns our predefined JSON. Running the tests should pass.
        response = mock_blog.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)

        # Additional assertions
        assert MockBlog is blog.Blog  # The mock is equivalent to the original

        assert MockBlog.called  # The mock wasP called

        mock_blog.posts.assert_called_with()  # We called the posts method with no arguments

        mock_blog.posts.assert_called_once_with()  # We called the posts method once with no arguments

        # blog.posts.assert_called_with(1, 2, 3) - This assertion is False and will fail since we called blog.posts with no arguments

        mock_blog.reset_mock()  # Reset the mock object

        mock_blog.posts.assert_not_called()  # After resetting, posts has not been called.


# Mock objects can also be reset to a pristine state i.e. the mock object has not been called yet. This is especially useful when you want to make multiple calls to your mock and want each one to run on a fresh instance of the mock.
if __name__ == '__main__':
    unittest.main()
