import pytest

from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator_header =                       self.page.locator('#header') ##locate top header section
        self.locator_products_button =              self.locator_header.locator(f"text=Products")
        self.locator_cart_button =                  self.locator_header.locator(f"text=Cart") ## in header section, find locator with text Cart
        self.locator_login_button =                 self.locator_header.locator(f"text=Signup / Login")
        self.locator_test_cases_button =            self.locator_header.locator(f"text=Test Cases")
        self.locator_API_testing_button =           self.locator_header.locator(f"text=API Testing")
        self.locator_video_tutorials_button =       self.locator_header.locator(f"text=Video Tutorials")
        self.locator_contact_us_button =            self.locator_header.locator(f"text=Contact us")

        self.locator_logout = self.locator_header.locator(f"text=Logout")
        self.locator_delete_account = self.locator_header.locator(f"text=Delete Account")

