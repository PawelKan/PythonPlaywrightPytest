from playwright.sync_api import Page, expect

from data.data_countries import COUNTRY
from pages.base_page import BasePage
from translations.en_texts_on_register_page import *

class RegisterAccountSuccessPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.header_account_created = page.locator(f'[data-qa="account-created"]')
        self.paragraph_first = page.locator('.col-sm-9.col-sm-offset-1 > p').first
        self.paragraph_last = page.locator('.col-sm-9.col-sm-offset-1 > p').last
        self.button_continue = page.locator(f'[data-qa="continue-button]')

    def get_header_text(self): return self.header_account_created.inner_text()
    def get_first_paragraph_text(self): return self.paragraph_first.inner_text()
    def get_last_paragraph_text(self): return self.paragraph_last.inner_text()
    def click_continue_button(self): self.button_continue.click()

