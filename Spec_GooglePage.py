from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.GooglePage import GooglePage
import unittest

class TestGooglePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_check_page_title(self):
        Google_page = GooglePage(self.driver)
        Google_page.openpage()
        page_title = Google_page.get_Title()
        self.assertIn("Google", page_title)

    def tearDown(self):
        self.driver.close()

#---START OF SCRIPT
#if __name__=="__main__":
#    suite = unittest.TestLoader().loadTestsFromTestCase (TestGooglePage)
#    unittest.TextTestRunner(verbosity=2).run(suite)
    #xmlrunner.XMLTestRunner(verbosity=2, output='reports').run(suite)