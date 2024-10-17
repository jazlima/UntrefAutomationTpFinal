from selenium.webdriver.common.by import By

class Page_Cart():
    def __init__(self,driver):
        self.driver = driver
        self.checkout_button = (By.ID,'checkout')

    def go_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()