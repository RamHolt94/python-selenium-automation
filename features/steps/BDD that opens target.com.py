from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# open the url
@given('Open Target main page')
def open_target(context):
    # context.driver.get('https://www.target.com/')
    context.app.main_page.open_main()


# find the cart icon and click
@when('Click on the cart icon')
def click_on_icon(context):
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='@web/CartLink']"))
    )
    element.click()


# Verify the cart is empty
@then('Verify the cart is empty')
def verify_cart(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='boxEmptyMsg']"))
    )


# Open target circle page
@given('Open Target Circle page')
def open_target(context):
    context.driver.get('https://www.target.com/circle')


# Find and count all target circle benefit cells
@when('Count the benefit cells')
def click_on_slingshot(context):
    result = len(context.driver.find_elements(By.CSS_SELECTOR, "div[class*='CellItemContainer']"))
    print(f"The amount of cells is {result}")


# Click target search bar
@when('Click search bar')
def click_search_bar(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']").click()


@when("Search for '{product_name}'")
def search_for_product(context, product_name):
    # context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']").send_keys(product_name)
    context.app.header.search_product(product_name)


@when('Click search icon')
def click_search_icon(context):
    element = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']"))
    )
    element.click()


@then('Add product to cart')
def add_to_cart(context):
    # element = WebDriverWait(context.driver, 10).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='product-title']"))
    # )
    # element.click()
    context.app.main_page.product_title()


@then('Click second button to add')
def click_second_button_add(context):
    # element = WebDriverWait(context.driver, 10).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label*='shipping']"))
    # )
    # element.click()
    context.app.main_page.second_add_button()


@then('Click view cart and check out')
def click_view_cart(context):
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label*='Add to cart for UNbrush']"))
    )
    element.click()

    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "*[text()='View cart']"))
    )
    element.click()


@then('Find the {total}')
def find_total(context, total):
    # cart_amount = context.driver.find_element(By.XPATH, "//p[text()='$25.43']")
    # print(cart_amount
    context.app.search_result_page.find_total(total)
