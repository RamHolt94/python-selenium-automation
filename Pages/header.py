from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Header(BasePage):
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "[aria-label*='sign in']")
    SECOND_SIGN_IN_BTN =(By.CSS_SELECTOR, "[data-test='accountNav-signIn']")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_INPUT)

        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SEARCH_BTN)
        )
        element.click()

    def find_sign_in(self):
        self.click(*self.SIGN_IN_BTN)

    def click_sign_in(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SECOND_SIGN_IN_BTN)
        )
        element.click()

        WebDriverWait(self.driver, 10).until(
            EC.url_contains('signin')
        )
        assert 'signin' in self.driver.current_url.lower(), f"Expected query not in {self.driver.current_url.lower()}"