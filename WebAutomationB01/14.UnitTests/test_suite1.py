import unittest

from test_case1 import TestCase1
from test_case2 import TestCase2

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCase2)

smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner().run(smoke_test)