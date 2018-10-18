# About:
This repo is an attempt to use Python, Pytest and Unittest, python-selenium to create automated testsuites.

This example uses the Page Object pattern to separate actual Test specs from Pages (a page represents a page under test, and all its UI elements)

## Requirements:
 1. python 3+
 2. selenium
 3. Pytest
 4. Unittest


## Running the tests:
  py.test --junitxml results.xml run.py

## To do:
  Modify the tests classes to take into account remote execution for selenium grid

## Results:
  a Junit-formatted xml file:
  
```xml
<?xml version="1.0" encoding="utf-8"?>
<testsuite errors="0" failures="0" name="pytest" skips="0" tests="3" time="53.296">
    <testcase classname="run2.TestGooglePage" file="Spec_GooglePage.py" line="10" name="test_check_page_title" time="24.370203018188477"></testcase>
    <testcase classname="run2.TestGooglePageTwo" file="Spec_GooglePageTwo.py" line="10" name="test_check_page_title" time="13.750821828842163"></testcase>
</testsuite>
