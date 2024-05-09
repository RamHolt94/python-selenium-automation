from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Header(BasePage):
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)