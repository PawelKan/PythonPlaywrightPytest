import pytest


class HomePage:
    def __init__(self, page):
        self.page = page
        self.header = page.locator('#header') ##locate top header section
        self.products_button = self.header.locator(f"text=Products")
        self.cart_button = self.header.locator(f"text=Cart") ## in header section, find locator with text Cart
    def navigate(self):
        self.page.goto("https://automationexercise.com/")

    def get_title(self):
        return self.page.title()

    def click_products(self):
        self.products_button.click()

    def click_cart_button(self):
        self.cart_button.click()

