import unittest
import filecmp

# Boundary from Right-BICEP is considered in the test cases
# Inverse relationship from Right-BICEP is considered in the test cases
# Error conditions from Right-BICEP is considered in the test cases by using assertions

class TestFilecmpCmp(unittest.TestCase):
    def test_different_content_shallow(self):
        # file0 = os.path.join(os.path.dirname(__file__), '../resources/file0.txt')
        # file1 = os.path.join(os.path.dirname(__file__), '../resources/file1.txt')
        file0 = "resources/file0.txt"
        file1 = "resources/file1.txt"

        # Compare the os.stat() signature i.e the metadata
        # of both files
        comp = filecmp.cmp(file0, file1)
        self.assertFalse(comp)

    def test_same_content_shallow(self):
        file0 = "resources/file0.txt"
        file1 = "resources/file0_copy.txt"

        # Compare the os.stat() signature i.e the metadata
        # of both files
        comp = filecmp.cmp(file0, file1)
        self.assertTrue(comp)

    def test_different_content_no_shallow(self):
        file0 = "resources/file0.txt"
        file1 = "resources/file1.txt"

        # Compare the contents of both files
        comp = filecmp.cmp(file0, file1, False)
        self.assertFalse(comp)

    def test_same_content_no_shallow(self):
        file0 = "resources/file0.txt"
        file1 = "resources/file0_copy.txt"

        # Compare the contents of both files
        comp = filecmp.cmp(file0, file1, False)
        self.assertTrue(comp)
