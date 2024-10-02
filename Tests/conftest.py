import pytest
from selenium import webdriver
@pytest.fixture(params=["chrome","edge"])
def setup_and_teardown(request):
    global driver
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "edge":
        driver=webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/v1/index.html")
    request.cls.driver=driver
    yield
    driver.quit()

