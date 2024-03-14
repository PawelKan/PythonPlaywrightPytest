import pytest
from playwright.sync_api import sync_playwright
@pytest.fixture(autouse=True, scope="function") ## fixture will be run for each method
def setup_browser_fixture():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

