import time

from selenium import webdriver

def setup_module(function):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()

def teardown_module(function):
    driver.quit()

def test_demotest1():

    driver.get("https://www.facebook.com/")
    time.sleep(5)


def test_demotest2():

    driver.get("https://www.amazon.com/")
    time.sleep(5)


def test_demotest3():

    driver.get("https://www.flipkart.com/")
    time.sleep(5)

def test_demotest4():

    driver.get("https://www.ajio.com/")
    time.sleep(5)


