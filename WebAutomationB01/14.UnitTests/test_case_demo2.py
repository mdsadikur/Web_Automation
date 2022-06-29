import unittest

'''
setUp and tearDown implemented on Class level
'''

class TestCaseDemo1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Browser launch.")

    def setUp(self):
        print("Open Login page.")

    def test_case_A(self):
        print("Login valid test Executed.")

    def test_case_B(self):
        print("Login Invalid test Executed.")

    def tearDown(self):
        print("Browser Close.")

    @classmethod
    def tearDownClass(cls):
        print("All Test case Execution Completed.")


if __name__ == '__main__':
    unittest.main()
