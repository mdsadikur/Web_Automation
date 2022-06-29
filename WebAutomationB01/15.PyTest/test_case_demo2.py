import pytest

@pytest.yield_fixture()
def setUp():
    print("setUp - Running once before test case.")
    yield
    print("tearDown - Running once after test case.")

def test_case_1(setUp):
    print("Test case 1 executed")

def test_case_2(setUp):
    print("Test case 2 executed")