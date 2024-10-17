from selenium.webdriver.common.by import By

class Page_Login():
    def __init__(self, driver):
        self.driver = driver
        self.user_name = (By.ID,'user-name')
        self.password = (By.ID,'password')
        self.login_button = (By.ID,'login-button')

    def login(self, usuario, password):
        self.driver.find_element(*self.user_name).send_keys(usuario)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()