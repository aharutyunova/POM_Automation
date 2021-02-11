from selenium import webdriver
import os
import sys 

class Base:

    def browser(self):
        browser = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        return browser

    def close_browser(self, browser):
        browser.quit()
    
    def get_file_name(self):
        filename=os.path.basename(sys.argv[0][:-3])
        print(sys.argv)
        print('test')
        return filename

    def save_screen(self, browser,current_file):
        browser.save_screenshot(f'{current_file}.png')
    
