from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Lib import LIB


class Contact_Us:

    #---locators---
    subject_heading      = (By.XPATH, '//select[@id="id_contact"]')
    email_address        = (By.ID, 'email')
    order_reference      = (By.ID, 'id_order')
    input_message_text   = (By.ID, 'message')
    send_button          = (By.ID, 'submitMessage')


    #---methods---
    def __init__(self, browser):
        self.browser = browser

    #choose subject heading
    def choose_subject_heading(self, browser):
        LIB.wait_for_element(self, browser, self.subject_heading)
        select_text = LIB.get_data(self, key = 'subject_heading')
        element = self.browser.find_element(*self.subject_heading)
        element.click()
        select = Select(element)
        select.select_by_visible_text(select_text)
        
    #input email address
    def input_email_address(self):
        email_value = LIB.get_data(self, key = 'valid_email')
        self.browser.find_element(*self.email_address).send_keys(email_value)


    #input order reference
    def input_order_referenc(self):
        reference_value = LIB.get_data(self, key = 'references')
        self.browser.find_element(*self.order_reference).send_keys(reference_value)

    #input message
    def input_message(self):
        message = LIB.get_data(self, 'contuct_us_input_message')
        self.browser.find_element(*self.input_message_text).send_keys(message)

    #click Send button
    def click_send_button(self):
        self.browser.find_element(*self.send_button).click()


