from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SeleniumEasy_Anna import testdata


class Main:
    def __init__(self, browser):
        self.browser = browser

    url             = testdata.data['url']
    main_tab        = (By.ID, "myTab")
    popup           = (By.ID, 'at-cv-lightbox-close')
    navigation_bar  = (By.ID, 'navbar-brand-centered')
    menu_list       = (By.XPATH, "//div[text()='Menu List']")
    main_menu_xpath = "//a[text()='%s']"
    sub_menu_xpath  = "//a[text()='Input Forms']//following::a[text()='%s']"
    

    def open_page(self):
        self.browser.get(self.url)
        self.browser.maximize_window()
        try:
            close_icon = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(self.popup))
            close_icon.click()
        except:
            pass
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_all_elements_located(self.navigation_bar))

    def select_menu_link(self, menu_link):
        menu_list_el = self.browser.find_element(*self.menu_list)
        self.browser.execute_script(
            "arguments[0].scrollIntoView(true);", menu_list_el)
        # Click Input Forms
        self.browser.find_element_by_xpath(self.main_menu_xpath % menu_link).click()
    
    def select_submenu(self, submenu_link):
        self.browser.find_element_by_xpath(self.sub_menu_xpath % submenu_link).click()
        # wait until submenu page is opened
        WebDriverWait(self.browser, 10).until(
            EC.invisibility_of_element_located(self.main_tab))

