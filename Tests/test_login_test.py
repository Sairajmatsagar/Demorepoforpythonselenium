import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://m.facebook.com/")
ww=WebDriverWait(driver,10)
time.sleep(3)
driver.find_element(By.CLASS_NAME,"dropbtn").click()
time.sleep(2)
facebook=ww.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,'Facebook')))
facebook.click()


time.sleep(15)