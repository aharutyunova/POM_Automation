from Lib import LIB
from POM.Home import Home
from pathlib import Path


'''
1. Go to URL
2. Click to Woment tab
3. Open file with 'log' name
4. Write there all found products name with their prices
5. Close browser
'''

def test_3():
    try:
        #open browser
        obj_lib = LIB()
        browser = obj_lib.open_browser()

        # navigate to url
        obj_lib.page_load(browser)

        #Create Home object
        obj_home = Home(browser)

        #wait and click on women tab
        obj_lib.wait_for_element(browser, obj_home.women_tab)
        browser.find_element(*obj_home.women_tab).click()

        #Product result
        product_result = obj_home.give_product_name_price(browser)
    
        #open file and write product list there
        obj_lib.write_to_file(product_result)

        print('Test run pass!')

    except Exception as e:
        print(e)
        obj_lib.save_screenshot(browser)
        print('Test run failed!')

    finally:
        #Close browser
        obj_lib.close_browser(browser)
            

