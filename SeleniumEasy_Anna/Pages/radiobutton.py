

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Radiobutton:


    def __init__(self, browser):
        self.browser = browser

    radiobutton_xpath       ="//button[@id='buttoncheck']/preceding::input[@value='%s']"
    get_checked_value_btn   =(By.ID,'buttoncheck')
    message                 =(By.XPATH,"//button[@id='buttoncheck']//following::p[@class='radiobutton']")
    
    
    
    def select_button(self, radiobutton):
        self.browser.find_element_by_xpath(self.radiobutton_xpath % radiobutton).click()
        self.browser.find_element(*self.get_checked_value_btn).click()

    def get_message_text(self):
        message=self.browser.find_element(*self.message).text
        return message



