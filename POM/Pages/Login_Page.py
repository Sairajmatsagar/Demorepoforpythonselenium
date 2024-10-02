from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username_textfield = (By.ID,"user-name")
        self.password_textfield = (By.ID,"password")
        self.login_button = (By.ID,"login-button")

    def enter_username(self,username):
        self.driver.find_element(self.username_textfield).send_keys(username)



