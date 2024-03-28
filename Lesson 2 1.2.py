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
driver.get('https://www.target.com/')

#click the sign in button
driver.find_element(By.XPATH, "//span[@class='styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3']").click()
sleep(5)
#Click SignIn from side navigation
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
sleep(4)
#find "Sign into your Target account” text
driver.find_element(By.XPATH, "//*[text()='Sign into your Target account']")
sleep(4)
#verify that the sign in button is displayed
driver.find_element(By.XPATH, "//button[@type='submit' and @id='login']").click()
print("Test passed")
driver.quit()