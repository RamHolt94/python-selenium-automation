from selenium.webdriver.common.by import By
from behave import given, when, then

from time import sleep


# open the url
@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


#find the cart icon and click
@when('Click on the cart icon')
def click_on_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()


#Verify the cart is empty
@then('Verify the cart is empty')
def verify_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")


#Open target circle page
@given('Open Target Circle page')
def open_target(context):
    context.driver.get('https://www.target.com/circle')





#Find and count all target circle benefit cells
@when('Count the benefit cells')
def click_on_slingshot(context):
    result = len(context.driver.find_elements(By.CSS_SELECTOR, "div[class*='CellItemContainer']"))
    print(f"The amount of cells is {result}")



#Click target search bar
@when('Click search bar')
def click_search_bar(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']").click()


@when('Search for {product_name}')
def search_for_product(context, product_name):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']").send_keys(product_name)


sleep(4)


@when('Click search icon')
def click_search_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()


sleep(6)


@then('Add product to cart')
def add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,
                                "[aria-label*='Add UNbrush Detangler Hair Brush']").click()


sleep(6)


@then('Click second button to add')
def click_second_button_add(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='shippingButton']").click()


@then('Click view cart and check out')
def click_view_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[class*='StyledBaseButtonInternal']").click()

sleep(4)


@then('Find the {total}')
def find_total(context, total):
    cart_amount = context.driver.find_element(By.XPATH, "//p[text()='$25.43']")
    print(cart_amount)