import unittest


class TestCase1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Test case 1 -> Browser launch.")

    def setUp(self):
        print("Test case 1 -> Open Login page.")

    def test_method_A(self):
        print("Test case 1 -> Login valid test Executed.")

    def test_method_B(self):
        print("Test case 1 -> Login Invalid test Executed.")

    def tearDown(self):
        print("Test case 1 -> Browser Close.")

    @classmethod
    def tearDownClass(cls):
        print("Test case 1 -> All Test method Execution Completed.")


if __name__ == '__main__':
    unittest.main()
