from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import os
import sys
from lib import LIB
from home import Home
from sign_in import Sign_In
from contact_us import Contact_Us
import pytest

def test_ContuctUs_fail():
    try:
## 1. Go to URL
        object_lib = LIB()
        browser = object_lib.OpenBrowser()
        object_lib.PageLoad(browser)

# 2. Click to Contact US sign_in_button
        object_home = Home(browser)
        contact_us_page = object_home.ContactUs(browser)

##browser.find_element(By.CSS_SELECTOR, "div#contact-link a").send_keys(Keys.ENTER)

# 3. Fill all fields besides Message in Contact Us and click on Send button
        object_contactus = Contact_Us(browser)
        object_contactus.FillFeilds(browser)

#object_contactus.FillText(browser)

        object_contactus.ClickSend(browser)

# 4. Validate that success message displayed
        assert "Your message has been successfully sent to our team." in browser.page_source
# 5. Close browser

    # except Exception as e:
    #     print(e)
    #     print("Test run Failed")

    finally:
        object_lib.CloseBrowser(browser)

# test_ContuctUs_fail()