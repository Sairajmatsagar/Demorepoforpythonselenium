import time

from selenium import webdriver

def test_demotest1():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.facebook.com/")
    time.sleep(5)


def test_demotest2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.com/")
    time.sleep(5)


def test_demotest3():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.flipkart.com/")
    time.sleep(5)

def test_demotest4():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.ajio.com/")
    time.sleep(5)


