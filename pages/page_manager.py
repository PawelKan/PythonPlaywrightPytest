from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_account_success_page import RegisterAccountSuccessPage
from pages.register_page import RegisterPage


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
