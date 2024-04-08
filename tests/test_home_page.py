import re
from idlelib import browser

import pytest
from playwright.sync_api import expect, Page, Browser

from pages.home_page import HomePage
from data.data_for_tests import DataForTest


class TestHomePage:

    @pytest.fixture(autouse=True, scope="function")
    def before_tests_fixture(self, page: Page):
        self.home_page = HomePage(page)
        self.home_page.navigate()
    @pytest.mark.smoke
    def test_title_texts_on_pages(self):
        """Assertions made with pytest (not playwright) for learning"""
        assert self.home_page.get_title() == DataForTest.HOME_PAGE_TITLE_TEXT

        self.home_page.click_on_products()
        assert self.home_page.get_title() == DataForTest.PRODUCTS_PAGE_TITLE_TEXT

        self.home_page.click_on_cart_button()
        assert self.home_page.get_title() == DataForTest.CART_PAGE_TITLE_TEXT

        self.home_page.click_on_login_button()
        assert self.home_page.get_title() == DataForTest.LOGIN_PAGE_TITLE_TEXT

        self.home_page.click_test_cases_button()
        assert self.home_page.get_title() == DataForTest.TEST_CASES_PAGE_TITLE_TEXT

        self.home_page.click_api_testing_button()
        assert self.home_page.get_title() == DataForTest.API_TESTING_PAGE_TITLE_TEXT
        ##self.home_page.locator_video_tutorials_button.click() ##turned off - page is going to youtube channel

        self.home_page.click_contact_us_button()
        assert self.home_page.get_title() == DataForTest.CONTACT_US_PAGE_TITLE_TEXT