import pytest
from playwright.sync_api import Page

from data import urls
from data.urls import Urls


@pytest.mark.usefixtures("data_texts_for_elements_fixture")
class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url=Urls.BASE_URL):
        self.page.goto(url)
        self.page.wait_for_load_state('load')

    def get_title(self):
        return self.page.title()

    def get_url(self):
        return self.get_url()




