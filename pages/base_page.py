import pytest
from playwright.sync_api import Page


@pytest.mark.usefixtures("data_texts_for_elements_fixture")
class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url="https://automationexercise.com/"):
        self.page.goto(url)
        self.page.wait_for_load_state('load')

    def get_title(self):
        return self.page.title()
