from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# open the url
# @given('Open Target main page')
# def open_target(context):
#     context.driver.get('https://www.target.com/')

#find sign in and click
@when('Find sign in')
def find_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()


#find and click sign in on nav side bar
@then('Click sign in on nav side bar')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    sleep(5)
    assert 'signin' in context.driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"

