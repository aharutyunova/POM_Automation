from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Lib import LIB


class Sign_in:


    #---locators---
    email_address    = (By.ID, 'email')
    password         = (By.ID, 'passwd')
    sign_in_btn      = (By.ID, 'SubmitLogin')
    my_account_title = (By.XPATH, "//h1[text()='My account']")
    
    
    #init
    def __init__(self, browser):
        self.browser = browser


