from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# open the url
# @given('Open Target main page')
# def open_target(context):
#     context.driver.get('https://www.target.com/')


#find sign in and click
@when('Find sign in')
def find_sign_in(context):
    # element = WebDriverWait(context.driver, 10).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='@web/AccountLink']"))
    # )
    # element.click()
    context.app.header.find_sign_in()


#find and click sign in on nav side bar
@then('Click sign in on nav side bar')
def click_sign_in(context):
    # element = WebDriverWait(context.driver, 10).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='accountNav-signIn']"))
    # )
    # element.click()
    #
    # WebDriverWait(context.driver, 10).until(
    #     EC.url_contains('signin')
    # )
    # assert 'signin' in context.driver.current_url.lower(), f"Expected query not in
    # {context.driver.current_url.lower()}"
    context.app.header.click_sign_in()
