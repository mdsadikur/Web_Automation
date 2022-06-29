import pytest

@pytest.fixture()
def setUp():
    print("Running demo 1 Setup")

def test_case_1(setUp):
    print("Test case 1 executed")

def test_case_2(setUp):
    print("Test case 2 executed")