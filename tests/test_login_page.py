import pytest
from playwright.sync_api import Page, expect
from data.data_users_credentials import UsersData
from data.urls import Urls
from pages.home_page import HomePage
from pages.login_page import LoginPage


class TestLoginPage:
    """test examples with playwright assertions"""
    @pytest.fixture(autouse=True, scope="function")
    def before_tests_fixture(self, page: Page):
        #Given
        self.home_page = HomePage(page)
        self.login_page = LoginPage(page)
        self.login_page.open_page()

    @pytest.mark.functional
    def test_login_into_page_with_correct_user_credentials(self):
        #When
        self.login_page.login_into_page(UsersData.VALID_USER_EMAIL, UsersData.VALID_USER_PASS)

        #Then
        expect(self.home_page.locator_logout).to_be_visible()
        expect(self.home_page.locator_delete_account).to_be_visible()

    @pytest.mark.functional
    def test_try_to_login_into_page_with_incorrect_user_mail(self):
        #When
        self.login_page.login_into_page("invalidUserEmail", UsersData.VALID_USER_PASS)

        #Then
        expect(self.home_page.locator_logout).not_to_be_visible()
        expect(self.home_page.locator_delete_account).not_to_be_visible()
    def test_try_to_login_into_page_with_incorrect_user_password(self):
        #When
        self.login_page.login_into_page(UsersData.VALID_USER_EMAIL, "invalidUserPassword123)(")

        #Then
        expect(self.home_page.locator_logout).not_to_be_visible()
        expect(self.home_page.locator_delete_account).not_to_be_visible()
