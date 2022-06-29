import unittest

'''
setUp and tearDown implemented on method level
'''

class TestCaseDemo1(unittest.TestCase):

    def setUp(self):
        # print("setUp - I will run once before every test case.")
        print("Browser launch.")
        print("Open Login page")

    def test_case_A(self):
        # print("Running Method A")
        print("Login valid test Executed.")

    def test_case_B(self):
        # print("Running Method B")
        print("Login Invalid test Executed.")

    def tearDown(self):
        # print('tearDown - I will run once after every test case.')
        print("Browser Close.")


if __name__ == '__main__':
    unittest.main()
