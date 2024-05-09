from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchResultPage(BasePage):
    SEARCH_RESULT_AMOUNT = (By.XPATH, "//p[text()='$25.43']")

    def find_total(self, total):
        cart_amount = self.find_element(By.XPATH, "//p[text()='$25.43']")
        assert total in cart_amount, f"Expected amount {total} but got {cart_amount}"
