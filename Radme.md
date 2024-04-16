## PROJECT STRUCTURE
- tests/: Contains the test scripts.
- pages/: Contains page objects or helpers for Playwright.
- pytest.ini: Pytest configuration file.
- allure_reports/: Directory where Allure test results are stored.

## CONFIGURATION FOR TESTS:
- Viewport width: 1920 px
- Viewport Height: 1080 px
- Headless

## RUN TESTS SCRIPTS:
- all tests CLI: 
    - pytest
- with markers CLI: pytest -m mark_name eg:
    - pytest -m functional
    - pytest -m smoke

## GENERATE HTML RAPORT WITH ALLURE:
- allure_reports/: folder name with test report 
- to generate HTML report use CLI: allure serve ./allure_reports