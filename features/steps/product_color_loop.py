from selenium.webdriver.common.by import By
from behave import when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('Click product')
def click_product(context):
    context.driver.find_element(By.CSS_SELECTOR,
                                "[data-test='product-title')]").click()


@then('Check product color')
def check_product_color(context):
    context.colors = context.driver.find_elements(By.CSS_SELECTOR,
                                                  "div[class*='styles__ButtonWrapper-sc-519sqw-1 clSiPU']")
    context.color_values = []
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class*='styles__ButtonWrapper-sc-519sqw-1 clSiPU']")))

    for color in context.colors:
        color.click()
        color_value = color.get_attribute("aria-label")
        context.color_values.append(color_value)

    print(context.color_values)