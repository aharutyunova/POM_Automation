from Lib import LIB
from POM.Contact_Us import Contact_Us
from POM.Home import Home
from selenium import webdriver


'''
1. Go to URL
2. Click to Contact US button
3. Fill all fields besides Message field in Contact Us
4. click on Send button
5. Check that Validate message displays 
6. Close browser
'''

def test_2():
    try:
        #open browser
        obj_lib = LIB()
        browser = obj_lib.open_browser()

        # navigate to url
        obj_lib.page_load(browser)

        #create contuct_us object
        obj_contuct_us = Contact_Us(browser)
        obj_home = Home(browser)

        #steps
        obj_home.click_contuct_us(browser)
        obj_contuct_us.choose_subject_heading(browser)
        obj_contuct_us.input_email_address()
        obj_contuct_us.input_order_referenc()
        obj_contuct_us.click_send_button()

        #Verify that validation message displayes
        success_message = obj_lib.get_data('contact_us_error_message')
        assert success_message in browser.page_source,obj_lib.save_screenshot(browser)
        print('Test run pass!')

    finally:
        #Close browser
        obj_lib.close_browser(browser)
            

