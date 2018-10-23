from PageObjects.GooglePage import GooglePage
import pytest

class TestGooglePage():

    def test_check_page_title(self, browser):
        self.Google_page = GooglePage(browser)
        self.Google_page.open_page()
        page_title = self.Google_page.get_Title()
        assert "Google" in page_title