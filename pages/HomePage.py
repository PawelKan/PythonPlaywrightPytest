import pytest

from pages.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator_header =                       self.page.locator('#header') ##locate top header section
        self.locator_products_button =              self.locator_header.locator(f"text=Products")
        self.locator_cart_button =                  self.locator_header.locator(f"text=Cart") ## in header section, find locator with text Cart
        self.locator_login_button =                 self.locator_header.locator(f"text=Signup / Login") ## in header section, find locator with text Signup / Login
        self.locator_test_cases_button =            self.locator_header.locator(f"text=Test Cases") ## in header section, find locator with text Cart
        self.locator_API_testing_button =           self.locator_header.locator(f"text=API Testing") ## in header section, find locator with text Cart
        self.locator_video_tutorials_button =       self.locator_header.locator(f"text=Video Tutorials") ## in header section, find locator with text Cart
        self.locator_contact_us_button =            self.locator_header.locator(f"text=Contact us") ## in header section, find locator with text Cart
