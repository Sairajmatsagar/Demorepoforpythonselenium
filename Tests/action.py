import pytest


def test_testace1():
    print("this  is testcase 1")


@pytest.mark.dependency(depends=["test-testcase1"])
def test_testcase2():
    print("this is testcase  2")