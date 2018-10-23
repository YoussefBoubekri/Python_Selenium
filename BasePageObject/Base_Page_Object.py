from selenium import webdriver
import pytest

class Page(object):
    def __init__(self, mydriver, base_url):
        self.base_url = base_url
        self.driver = mydriver
        self.timeout = 30

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def open(self,url):
        url = self.base_url + url
        self.driver.get(url)
    
    def get_Title(self):
        return self.driver.title

