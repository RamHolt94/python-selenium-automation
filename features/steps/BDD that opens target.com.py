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
