# About:
This repo is an attempt to use Python, Pytest, and python-selenium package to create automated testsuites.

This example uses the Page Object pattern to separate actual Test specs from Pages (a page represents a page under test, and all its UI elements)

## Requirements:
 1. python 3+
 2. selenium
 3. Pytest

## Running the tests:
  py.test --junitxml results.xml run.py

## Note:
due to pytest fixture that accepts browsers dicts, and because that is injected directly using
pytest. tests specs will run for each pair key/value in those disctionaries.

```python
BROWSERS = {
    'firefox': webdriver.DesiredCapabilities.FIREFOX,
    'chrome': webdriver.DesiredCapabilities.CHROME,
}
...
```python

so when running tests in directmode (not through selenium hub), one should pass a dirver directly
then omit the browser arg in the fixture function
```python
@pytest.fixture(params=BROWSERS.keys())
def browser(request):
```python

## Results:
  a Junit-formatted xml file:
  
```xml
<?xml version="1.0" encoding="utf-8"?>
<testsuite errors="0" failures="0" name="pytest" skips="0" tests="3" time="53.296">
    <testcase classname="run2.TestGooglePage" file="Spec_GooglePage.py" line="10" name="test_check_page_title" time="24.370203018188477"></testcase>
    <testcase classname="run2.TestGooglePageTwo" file="Spec_GooglePageTwo.py" line="10" name="test_check_page_title" time="13.750821828842163"></testcase>
</testsuite>
