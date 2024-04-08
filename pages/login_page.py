from data.urls import Urls
from pages.base_page import BasePage
from playwright.sync_api import ElementHandle, Page


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.login_form_section = page.locator(".login-form")
        self.login_into_account_heading_locator = self.login_form_section.locator('h2') #with text Login to your account
        self.email_address_locator = self.login_form_section.locator('[data-qa="login-email"]')
        self.password_locator = self.login_form_section.locator('[data-qa="login-password"]')
        self.login_button = self.login_form_section.locator('[data-qa="login-button"]')

        self.new_user_signup_section = page.locator('.signup-form')
        self.new_user_signup_heading = self.new_user_signup_section.locator("h2")
        self.new_user_name_locator = self.new_user_signup_section.locator('[data-qa="signup-name"]')
        self.new_user_email_address_locator = self.new_user_signup_section.locator('[data-qa="signup-email"]')
        self.signup_button_locator = self.new_user_signup_section.locator('[data-qa="signup-button"]')

    def open_page(self):
        super().navigate(Urls.LOGIN_PAGE_URL)
    def login_into_page(self, user_email, user_password):
        self.email_address_locator.type(user_email)
        self.password_locator.type(user_password)
        self.login_button.click()

    def fill_sign_up_form(self, name, email_address):
        self.new_user_name_locator.type(name)
        self.new_user_email_address_locator.type(email_address)
        self.signup_button_locator.click()

