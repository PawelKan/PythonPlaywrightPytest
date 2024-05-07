## Installation
- Clone this repository:
  - git clone git@github.com:PawelKan/PythonPlaywrightPytest.git
- Navigate to the project directory
- Install Python dependencies
  - pip install -r requirements.txt

## INFORMATION
- Page displays randomly adverts which can break tests.

## PROJECT STRUCTURE
- tests/: Contains the test scripts.
- pages/: Contains page objects or helpers for Playwright.
- pytest.ini: Pytest configuration file.
- allure_reports/: Directory where Allure test results are stored.

## CONFIGURATION FOR TESTS:
- Default Viewport width: 1920 px
- Default Viewport Height: 1080 px
- Headless

## RUN TESTS SCRIPTS:
- all tests CLI: 
    - pytest
- with markers CLI: pytest -m mark_name eg:
    - pytest -m functional
    - pytest -m smoke
- run tests parallel with xdist library:
  - run with maximum workers (threads) - pytest -n auto
  - run with custom number of threads - pytest -n 6
- run tests with all browsers (chromium, firefox, webkit) AND with parallel
  - pytest --browser chromium --browser firefox --browser webkit -n auto
- run tests on mobile like "Chromium"
  - pytest --device "Galaxy Note 3"
- run tests with custom viewport size
  - pytest --width=1440 --height=800


## GENERATE HTML RAPORT WITH ALLURE:
- allure_reports/: folder name with test report 
- to generate HTML report use CLI: allure serve ./allure_reports
