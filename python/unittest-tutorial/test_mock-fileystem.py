from filesystem import (rm, rm_smarter, RemovalService, UploadService)

import os.path
import tempfile
import unittest
from unittest.mock import patch


# Our test case is pretty simple, but every time it is run, a temporary file is created and then deleted. Additionally, we have no way of testing whether our rm method properly passes the argument down to the os.remove call. We can assume that it does based on the test above, but much is left to be desired.
@unittest.skip("slow cold for system call. namely filesystem and network access.")
class RmTestCase(unittest.TestCase):
    tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")

    def setUp(self):
        # This means that all data read from the file is returned as bytes objects, not str.
        # see https://stackoverflow.com/questions/33054527/typeerror-a-bytes-like-object-is-required-not-str-when-handling-file-conte
        with open(self.tmpfilepath, "wb") as f:
            f.write(b"Delete me!")

    def test_rm(self):
        # remove the file
        rm(self.tmpfilepath)
        # test that it was actually removed
        self.assertFalse(os.path.isfile(self.tmpfilepath), "Failed to remove the file.")


# With these refactors, we have fundamentally changed the way that the test operates. Now, we have an insider, an object we can use to verify the functionality of another.
class RmMockTestCase(unittest.TestCase):

    @patch('filesystem.os')
    def test_rm(self, mock_os):
        rm("any path")
        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("any path")


# Test rm_smarter
# let’s adjust our test case to keep coverage up.
class RmSmarterMockTestCase(unittest.TestCase):

    @patch('filesystem.os.path')
    @patch('filesystem.os')
    def test_rm_smarter(self, mock_os, mock_path):
        # set up the mock
        mock_path.isfile.return_value = False

        rm_smarter("any path")

        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")

        # make the file 'exist'
        mock_path.isfile.return_value = True

        rm_smarter("any path")

        mock_os.remove.assert_called_with("any path")


# You'll notice that not much has changed in our test case:


class RemovalServiceTestCase(unittest.TestCase):

    @patch("filesystem.os.path")
    @patch("filesystem.os")
    def test_rm(self, mock_os, mock_path):
        # instantiate our service
        reference = RemovalService()

        # set up the mock
        mock_path.isfile.return_value = False

        reference.rm("any path")

        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")

        # make the file 'exit'
        mock_path.isfile.return_value = True

        reference.rm("any path")
        mock_os.remove.assert_called_with("any path")


# Since we already have test coverage on the RemovalService, we’re not going to validate internal functionality of the rm method in our tests of UploadService. Rather, we’ll simply test (without side-effects, of course) that UploadService calls the RemovalService.rm method, which we know “just works™” from our previous test case.

# There are two ways to go about this:

# 1. Mock out the RemovalService.rm method itself.
# 2. Supply a mocked instance in the constructor of UploadService.

# As both methods are often important in unit-testing, we’ll review both.

class UploadServiceTestCase(unittest.TestCase):
    # Mocking the specific instance method
    @patch.object(RemovalService, "rm")
    def test_upload_complete(self, mock_rm):
        # build our dependencies
        removal_service = RemovalService()
        reference = UploadService(removal_service)

        # call upload_complete, which should, in turn, call `rm`:
        reference.upload_complete("my uploaded file")

        # check that it called the rm method of any RemovalService
        mock_rm.assert_called_with("my uploaded file")

        # check that it called the rm method of _our_ removal_service
        removal_service.rm.assert_called_with("my uploaded file")

        # Great! We’ve validated that the UploadService successfully calls our instance’s rm method. Notice anything interesting in there? The patching mechanism actually replaced the rm method of all RemovalService instances in our test method. That means that we can actually inspect the instances themselves. If you want to see more, try dropping in a breakpoint in your mocking code to get a good feel for how the patching mechanism works.

    # Instead of mocking the specific instance method, we could instead just supply a mocked instance to UploadService with its constructor.
    # The mock.create_autospec method creates a functionally equivalent instance to the provided class. What this means, practically speaking, is that when the returned instance is interacted with, it will raise exceptions if used in illegal ways. More specifically, if a method is called with the wrong number of arguments, an exception will be raised. This is extremely important as refactors happen. As a library changes, tests break and that is expected. Without using an auto-spec, our tests will still pass even though the underlying implementation is broken.
    def test_upload_complete_mock_object(self):
        # build our dependencies
        mock_removal_service = unittest.mock.create_autospec(RemovalService)
        reference = UploadService(mock_removal_service)

        # call upload_complete, which should, in turn, call `rm`:
        reference.upload_complete("my uploaded file")

        # test that it called the rm method
        mock_removal_service.rm.assert_called_with("my uploaded file")


if __name__ == '__main__':
    unittest.main()
