
# from selenium import webdriver
from SeleniumEasy_Anna.lib import Base
from SeleniumEasy_Anna.Pages.mainpage import Main
from SeleniumEasy_Anna.Pages.radiobutton import Radiobutton
from SeleniumEasy_Anna import testdata
import sys



try:
#Activate Chrome browser
    base_page=Base()
    browser = base_page.browser()

    # Set up test case data
    submenu_link          = testdata.data['submenu']
    select_menu_link      = testdata.data['mainmenu']
    radiobutton           = testdata.data['radiobutton']


    # Create Main class object and use class's methods
    main=Main(browser)
    main.open_page()
    main.select_menu_link(select_menu_link)
    main.select_submenu(submenu_link)

    # Create Radiobutton class object and use class's methods
    rdb=Radiobutton(browser)
    rdb.select_button(radiobutton)

    # get current filename
    filename=base_page.get_file_name()
    # Verify that message is correcspond to selected radiobutton

    assert radiobutton in rdb.get_message_text(), base_page.save_screen(browser,filename)
    print('uraaaaa')
    Print('uraaaaa 5555')
finally:
    base_page.close_browser(browser)

