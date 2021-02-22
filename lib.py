from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import os
import sys



class LIB():
# with open('config.json') as f:
#     data = json.load(f)
# #email_address = data['eMail']
#     # def LoadConfig(self):
#     #     with open('config.json') as f:
#     #         data = json.load(f)
#     #     return data  

    def OpenBrowser(self):
        try: 
            with open('config.json') as f:
                data = json.load(f)
            browser = webdriver.Chrome(data['driver_path'])
            browser.maximize_window()
            return browser
        except:
            print('Something went wrong')

    def PageLoad(self, browser):
        try: 
            with open('config.json') as f:
                data = json.load(f)
            browser.get(data["web_page_address"])
        except:
            print('Something went wrong!')

    def MoveToElement(self, browser, element):
        
        action = ActionChains(browser)
        action.move_to_element(element).perform()            
           

    def WaitForElements(self, browser, elements):
        try:
            WebDriverWait(browser,30).until(EC.visibility_of_any_elememts_located(elements))
        except:
            print("Elements are not visible")
    
    def WaitForElement(self, browser, element):
        try:
            WebDriverWait(browser,10).until(EC.visibility_of_any_elememt_located(element))
        except:
            print("Element is not visible")    

    def Data(self, key):
        try: 
            with open('data.json') as f:
                data = json.load(f)
            return data[key]
        except:
            print('Error while getting data.')

    def SaveScreenshot(self, browser):
        current_filename=os.path.basename(sys.argv[0][:-3])
        try:
            browser.save_screenshot(f"Test\\{current_filename}_screenshot.png")
        except:
            print("Screenshot is not saved")

    def CloseBrowser(self, browser):
        try:
            browser.quit()
        except:
            print("Driver is not closed")
