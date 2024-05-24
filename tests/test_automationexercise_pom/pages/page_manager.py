from playwright.sync_api import Page

from tests.test_automationexercise_pom.pages.home_page import HomePage
from tests.test_automationexercise_pom.pages.login_page import LoginPage
from tests.test_automationexercise_pom.pages.register_account_success_page import RegisterAccountSuccessPage
from tests.test_automationexercise_pom.pages.register_page import RegisterPage


class PageManager:
    def __init__(self, page: Page):
        self.__home_page = HomePage(page)
        self.__login_page = LoginPage(page)
        self.__register_page = RegisterPage(page)
        self.__success_page_after_registration = RegisterAccountSuccessPage(page)

    def on_home_page(self): return self.__home_page

    def on_login_page(self): return self.__login_page

    def on_register_page(self): return self.__register_page

    def on_success_page_after_registration(self): return self.__success_page_after_registration
