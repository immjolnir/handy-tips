import unittest
import os


class GetLastPartOfPath(unittest.TestCase):
    test_path = '/folderA/folderB/folderC/folderD/'

    def test_basename(self):
        """
        https://docs.python.org/3/library/os.path.html#os.path.basename
        Return the base name of pathname path. This is the second element of the pair returned by passing path to the function split(). Note that the result of this function is different from the Unix basename program; where basename for '/foo/bar/' returns 'bar', the basename() function returns an empty string ('').
        """
        path = os.path.basename(self.test_path)
        self.assertEqual(path, "")

        self.assertEqual(os.path.basename("A//B"), "B")
        self.assertEqual(os.path.basename("A//B/"), "")

    def test_normpath(self):
        """
        os.path.normpath
        https://docs.python.org/3/library/os.path.html#os.path.normpath

        Normalize a pathname by collapsing redundant separators and up-level references so that A//B, A/B/, A/./B and A/foo/../B all become A/B. This string manipulation may change the meaning of a path that contains symbolic links.
        """
        self.assertEqual(os.path.normpath("A//B"), "A/B")
        self.assertEqual(os.path.normpath("A/B"), "A/B")
        self.assertEqual(os.path.normpath("A/./B"), "A/B")
        self.assertEqual(os.path.normpath("A/foo/../B"), "A/B")

    def test_basename_normapth_chain(self):
        path = os.path.basename(os.path.normpath(self.test_path))
        self.assertEqual(path, "folderD")


# Run it like this:
# $ python3 get-last-part-of-path.py  -v
if __name__ == '__main__':
    unittest.main()
