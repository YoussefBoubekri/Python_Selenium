from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from BasePageObject.Base_Page_Object import Page

class GooglePage(Page):
    #Elements
    url = ""
    #Locators
    search_text_box = (By.ID, 'lst-ib')
    search_button = (By.CSS_SELECTOR, 'input[type="submit"]')
 
    def __init__(self, selenium_driver,base_url='http://www.google.fr/'):
        Page.__init__(self, selenium_driver, base_url='http://www.google.fr/') 

    # Actions
    def openpage(self):
        self.open(self.url)

    def get_Title(self):
        """Returns the page title"""        
        return self.driver.title

    def execute_search(self, search_query):
        """Clicks the end of game button"""
        self.find_element(*self.search_text_box).send_keys(search_query)
        self.find_element(*self.search_button).click()