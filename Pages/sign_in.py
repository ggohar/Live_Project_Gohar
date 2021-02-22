from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from lib import LIB
import json
from selenium.webdriver.support.ui import WebDriverWait

class Sign_In:
    def __init__(self, browser):
        self.browser = browser

#locators
    email_address = (By.ID, "email")
    password = (By.ID, "passwd")
    sign_in_button = (By.ID, "SubmitLogin")
    my_account_tytle = (By.XPATH, "//span[text()='My account']")

    def LoginPass(self, browser):
        with open('config.json') as f:
            data = json.load(f)
        browser.find_element(By.ID, "email").send_keys("gogimar92@gmail.com")
        browser.find_element(By.ID, "passwd").send_keys("gogijan92")

    def ClickSignIn(self, browser):
        element = self.browser.find_element(*self.sign_in_button)
        LIB.MoveToElement(self, browser, element)
        browser.find_element(By.ID, "SubmitLogin").send_keys(Keys.ENTER)
