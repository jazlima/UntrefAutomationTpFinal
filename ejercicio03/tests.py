import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from dotenv import load_dotenv
import os
from selenium.webdriver.firefox.options import Options

from pages.page_login import Page_Login
from pages.page_inventory import Page_Inventory
from pages.page_cart import Page_Cart
from pages.page_checkout import Page_Checkout

class Compras(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        options = Options()
        options.add_argument('--incognito')
        options.add_argument('--headless')
        cls.driver = webdriver.Firefox(options = options)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
    
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        load_dotenv()
        base_url = os.getenv('BASE_URL')
        user = os.getenv('USER')
        password = os.getenv('PASS')
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.driver.get(base_url)
        page_login = Page_Login(self.driver)
        page_login.login(user,password)
        self.page_inventory = Page_Inventory(self.driver)

    def tearDown(self) -> None:
       self.driver.close()
       self.driver.quit()

    def test_order_price_lohi(self):
        self.page_inventory.select_order_by_visible_text('Price (low to high)')
        prices = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
        prices_list = [float(price.text.replace('$', '')) for price in prices]
        self.assertEqual(prices_list, sorted(prices_list))

    def test_buy_error(self):
        add_buttons = self.driver.find_elements(By.CLASS_NAME, 'btn_inventory')
        for button in add_buttons:
               button.click()
        self.page_inventory.go_to_cart()
        page_cart = Page_Cart(self.driver)
        self.driver.find_element(By.ID, 'shopping_cart_container').click()
        productos = self.driver.find_elements(By.CLASS_NAME, 'cart_item')
        self.assertEqual(len(productos), len(add_buttons))
        page_cart.go_to_checkout()
        page_checkout = Page_Checkout(self.driver)
        self.driver.find_element(By.ID, 'first-name').send_keys('Jazmin')
        self.driver.find_element(By.ID, 'continue').click()
        message = page_checkout.get_error_message()
        self.assertEqual('Error: Last Name is required', message)
        self.driver.find_element(By.ID, 'last-name').send_keys('Rivas')
        self.driver.find_element(By.ID, 'continue').click()
        message = page_checkout.get_error_message()
        self.assertEqual('Error: Postal Code is required', message)
        
    def test_buy_ok(self):
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
        self.page_inventory.go_to_cart()
        self.driver.find_element(By.ID, 'remove-sauce-labs-bike-light').click()
        cart_items = self.driver.find_elements(By.CLASS_NAME, 'cart_item')
        self.assertEqual(len(cart_items), 0, 'Aún hay artículos en el carrito.')
        self.driver.find_element(By.ID, 'continue-shopping').click()
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
        self.page_inventory.go_to_cart()
        cart_items = self.driver.find_elements(By.CLASS_NAME, 'cart_item')
        self.assertEqual(len(cart_items), 2)
        page_cart = Page_Cart(self.driver)
        page_cart.go_to_checkout()
        page_checkout = Page_Checkout(self.driver)
        page_checkout.checkout('Jazmin', 'Rivas', '1234')
        self.driver.find_element(By.ID, 'finish').click()
        message = page_checkout.get_final_message()
        self.assertEqual('Thank you for your order!', message)