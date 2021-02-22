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
from Pages.home import Home
from Pages.sign_in import Sign_In
import pytest


def test_SignIn():
    try:
    ## Step 1) Open Chrome browser
        object_lib = LIB()
        browser = object_lib.OpenBrowser()

    ## 2) Go to URL
        object_lib.PageLoad(browser)

    ## 3) Click to Sign In in Home page

        object_home = Home(browser)
        object_home.OpenSignIn(browser)

    ## 4) Fill email address and password
        object_signin = Sign_In(browser)
        object_signin.LoginPass(browser)

    ## 5)Click Sign In sign_in_button
        object_signin.ClickSignIn(browser)

    ## 6) Verify that you signed successfully
        assert "My account" in browser.title
        
        print("Test run Passed!")

    # except Exception as e:
    #     print(e)
    #     print("Test run Failed")

    finally:
        object_lib.CloseBrowser(browser)

test_SignIn()

