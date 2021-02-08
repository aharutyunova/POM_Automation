from Seleniumeasy.pages.Base_page import Base
from Seleniumeasy.pages.menu_list import GoRadiobuttonsPage
from Seleniumeasy.pages.radiobutton_page import ClickRadiobuttons

# Activate Chrome browser
driver = Base().driver()

# Set up test case data
WORD = 'Male'

menu_list = GoRadiobuttonsPage(driver)
menu_list.load()

# Close opened popup, if popup exist
menu_list.close_popup()

# Scroll to Menu List
menu_list.scroll_to_menu_list()

# Click on "Radio buttons Demo"
menu_list.open_radiobutton_demo()

# Choose Male Radiobutton under "Radio Button Demo" section
radiobutton_page = ClickRadiobuttons(driver)
radiobutton_page.click_radiobutton_male()

# Click Get check value button
radiobutton_page.click_button_check()

# Check that Male word exist in message, if not, save screenshot
radiobutton_page.check_word(WORD)

# close browser
driver.close()