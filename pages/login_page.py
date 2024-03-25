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

    def login_into_page(self, user_email, user_password):
        self.email_address_locator.type(user_email)
        self.password_locator.type(user_password)
        self.login_button.click()
