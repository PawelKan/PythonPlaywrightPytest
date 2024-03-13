import pytest
from playwright.sync_api import sync_playwright
@pytest.fixture(autouse=True, scope="session")
def setup_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield page
        browser.close()
