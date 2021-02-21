from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from lib import LIB
import json

## locators
 #   email_address = (By.ID, 'email')
 #   # password = (By.ID, 'passwd')
 #   # sign_in_button = (By.ID, 'SubmitLogin')
 #   # my_account_tytle = (By.XPATH, "//span[text()='My account']")
sign_in_page = (By.CSS_SELECTOR, "a.login[title*='customer account']")
contact_us_button = (By.CSS_SELECTOR, "div#contact-link a")

class Home:
    def __init__(self, browser):
        self.browser = browser


    def OpenSignIn(self, browser): 
        try:
            browser.find_element(By.CSS_SELECTOR, "a.login[title*='customer account']").send_keys(Keys.ENTER)
        except:
            print("No element found")

    def ContactUs(self, browser): 
        try:
            browser.find_element(By.CSS_SELECTOR, "div#contact-link a").send_keys(Keys.ENTER)
        except:
            print("No element found")
