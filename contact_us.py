from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from lib import LIB
import json
import time

class Contact_Us:
    def __init__(self, browser):
        self.browser = browser


## locators
    contact_us_button = (By.ID, "contact-link")
    password = (By.ID, "passwd")
    sign_in_button = (By.ID, "SubmitLogin")
    my_account_tytle = (By.XPATH, "//span[text()='My account']")

    def ClickContactUs(self, browser):
        browser.find_element(By.ID, "contact-link").send_keys(Keys.ENTER)

    def FillFeilds(self, browser):
        select = Select(browser.find_element(By.CSS_SELECTOR, "select#id_contact"))
        select.select_by_value('2')
        browser.find_element(By.ID, 'email').send_keys("gogimar92@gmail.com")

    def FillText(self, browser):
        text = browser.find_element(By.CSS_SELECTOR, "textarea#message")
        text.send_keys("To Be or Not To Be... ")

    def ClickSend(self, browser):
        LIB.MoveToElement(self, browser, self.contact_us_button)
        element = self.browser.find_element(*self.contact_us_button)
        browser.find_element(By.ID, "submitMessage").send_keys(Keys.ENTER)



