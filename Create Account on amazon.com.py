from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com')
sleep(4)

#click account & lists dropdown then click create account button
driver.find_element(By.ID, 'nav-link-accountList').click()
sleep(4)
driver.find_element(By.ID, 'createAccountSubmit').click()
sleep(4)


#find the amazon icon
driver.find_element(By.CSS_SELECTOR, 'a.a-link-nav-icon')
sleep(3)
#find your name field
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
sleep(4)
# find mobile number field
driver.find_element(By.CSS_SELECTOR, '#ap_email')
sleep(4)
# find password field
driver.find_element(By.CSS_SELECTOR, "input[class*='auth-require-password-validation']")
sleep(4)
#
# find re-enter password field
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
sleep(5)
#find continue button
driver.find_element(By.CSS_SELECTOR, 'input.a-button-input')
sleep(3)
#find conditions of use
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")
sleep(4)
#find privacy notice
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")
sleep(4)

#find sign in
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis")
sleep(4)

driver.quit()
print("Test Success")