import pytest
from playwright.sync_api import Page
from data.data_users_credentials import UsersData
from data.urls import Urls
from pages.home_page import HomePage
from pages.login_page import LoginPage


class TestLoginPage:

    @pytest.fixture(autouse=True, scope="function")
    def before_tests_fixture(self, page: Page):
        self.home_page = HomePage(page)
        self.login_page = LoginPage(page)
        self.login_page.navigate(Urls.LOGIN_PAGE_URL)

    @pytest.mark.functional
    def test_login_into_page_with_correct_user_credentials(self):
        self.login_page.login_into_page(UsersData.VALID_USER_EMAIL, UsersData.VALID_USER_PASS)
        assert self.home_page.locator_logout.is_visible()
        assert self.home_page.locator_delete_account.is_visible()


