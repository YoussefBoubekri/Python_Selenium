from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from BasePageObject.Base_Page_Object import Page

class GooglePage(Page):
    #Elements
    url = "" # base url + /page.php... for any additional url request....
    search_button = (By.CSS_SELECTOR, 'input[type="submit"]')
 
    def __init__(self, driver):
        self.driver = driver 
        Page.__init__(self, self.driver, base_url='http://www.google.fr/')

    # Actions
    def open_page(self):
        self.open(self.url)

    def execute_search(self, search_query):
        self.find_element(*self.search_text_box).send_keys(search_query)
        self.find_element(*self.search_button).click()