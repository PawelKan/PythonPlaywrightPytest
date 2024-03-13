import pytest

from pages.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.header = self.page.locator('#header') ##locate top header section
        self.products_button = self.header.locator(f"text=Products")
        self.cart_button = self.header.locator(f"text=Cart") ## in header section, find locator with text Cart

    def click_products(self):
        self.products_button.click()

    def click_cart_button(self):
        self.cart_button.click()

