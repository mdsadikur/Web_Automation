import unittest


class TestCase2(unittest.TestCase):

    def setUp(self):
        print("Test case 2 -> Open Login page.")

    def test_method_A(self):
        print("Test case 2 -> Login valid test Executed.")

    def test_method_B(self):
        print("Test case 2 -> Login Invalid test Executed.")

    def tearDown(self):
        print("Test case 2 -> Browser Close.")


if __name__ == '__main__':
    unittest.main()
