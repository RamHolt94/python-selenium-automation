from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
    ADD_TO_CART = (By.CSS_SELECTOR, "[aria-label*='shipping']")

    def open_main(self):
        self.driver.get('https://www.target.com/')

    def product_title(self):
        self.click(*self.PRODUCT_TITLE)

    def second_add_button(self):
        self.click(*self.ADD_TO_CART)
