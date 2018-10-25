import pytest
from selenium import webdriver

BROWSERS = {
    'firefox': webdriver.DesiredCapabilities.FIREFOX,
    'chrome': webdriver.DesiredCapabilities.CHROME,
}

WEBDRIVER_ENDPOINT = 'http://localhost:4444/wd/hub'

@pytest.fixture(params=BROWSERS.keys())
def browser(request):
    driver = webdriver.Remote(
        command_executor=WEBDRIVER_ENDPOINT,
        desired_capabilities=BROWSERS[request.param]
    )
    #driver = webdriver.Chrome() # run locally for a quick test
    yield driver
    driver.quit()
