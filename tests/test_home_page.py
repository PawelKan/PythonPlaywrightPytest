import re
from idlelib import browser

import pytest
from playwright.sync_api import expect, Page, Browser

from data.urls import Urls
from pages.home_page import HomePage
from data.texts_on_pages import TextsOnPages
from pages.page_manager import PageManager

class TestHomePage:

    @pytest.fixture(autouse=True, scope="function")
    def before_tests_fixture(self, page: Page):
        self.pm = PageManager(page)
        self.pm.on_home_page().navigate()
    @pytest.mark.smoke
    def test_title_texts_on_pages(self):
        """Assertions made with pytest (not playwright) for learning"""
        assert self.pm.on_home_page().get_title() == TextsOnPages.HOME_PAGE_TITLE_TEXT

        self.pm.on_home_page().click_products()
        self.pm.on_home_page().page.wait_for_url(Urls.PRODUCTS_PAGE_URL)
        assert self.pm.on_home_page().get_title() == TextsOnPages.PRODUCTS_PAGE_TITLE_TEXT

        self.pm.on_home_page().click_cart_button()
        self.pm.on_home_page().page.wait_for_url(Urls.CART_PAGE_URL)
        assert self.pm.on_home_page().get_title() == TextsOnPages.CART_PAGE_TITLE_TEXT

        self.pm.on_home_page().click_login_button()
        self.pm.on_home_page().page.wait_for_url(Urls.LOGIN_PAGE_URL)
        assert self.pm.on_home_page().get_title() == TextsOnPages.LOGIN_PAGE_TITLE_TEXT

        self.pm.on_home_page().click_test_cases_button()
        self.pm.on_home_page().page.wait_for_url(Urls.TEST_CASES_PAGE_URL)
        assert self.pm.on_home_page().get_title() == TextsOnPages.TEST_CASES_PAGE_TITLE_TEXT

        self.pm.on_home_page().click_api_testing_button()
        self.pm.on_home_page().page.wait_for_url(Urls.API_TESTING_PAGE_URL)
        assert self.pm.on_home_page().get_title() == TextsOnPages.API_TESTING_PAGE_TITLE_TEXT
        ##self.pm.on_home_page().locator_video_tutorials_button.click() ##turned off - page is going to youtube channel

        self.pm.on_home_page().click_contact_us_button()
        self.pm.on_home_page().page.wait_for_url(Urls.CONTACT_US_PAGE_URL)
        assert self.pm.on_home_page().get_title() == TextsOnPages.CONTACT_US_PAGE_TITLE_TEXT