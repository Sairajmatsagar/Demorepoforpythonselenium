import pytest


@pytest.fixture
def beforetest_and_aftertest():
    print("launch browser")
    print("open application")
    yield
    print("logout")
    print("closed browser")
