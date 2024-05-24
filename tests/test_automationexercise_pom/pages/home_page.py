from playwright.sync_api import Page

from data.urls import Urls
from tests.test_automationexercise_pom.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        """Initialize locators for different buttons in the header section."""
        self.locator_header = self.page.locator('#header') ##locate top header section
        self.locator_products_button = self.locator_header.locator(f"text=Products")
        self.locator_cart_button = self.locator_header.locator(f"text=Cart") ## in header section, find locator with text Cart
        self.locator_login_button = self.locator_header.locator(f"text=Signup / Login")
        self.locator_test_cases_button = self.locator_header.locator(f"text=Test Cases")
        self.locator_api_testing_button = self.locator_header.locator(f"text=API Testing")
        self.locator_video_tutorials_button = self.locator_header.locator(f"text=Video Tutorials")
        self.locator_contact_us_button = self.locator_header.locator(f"text=Contact us")

        self.locator_logout_button = self.locator_header.locator(f"text=Logout")
        self.locator_delete_account_button = self.locator_header.locator(f"text=Delete Account")

    def open_page(self):
        super().navigate(Urls.BASE_URL)
    def click_products(self): self.locator_products_button.click()
    def click_cart_button(self): self.locator_cart_button.click()
    def click_login_button(self): self.locator_login_button.click()
    def click_test_cases_button(self): self.locator_test_cases_button.click()
    def click_api_testing_button(self): self.locator_api_testing_button.click()
    def click_video_tutorials_button(self): self.locator_video_tutorials_button.click()
    def click_contact_us_button(self): self.locator_contact_us_button.click()
    def click_logout_button(self): self.locator_logout_button.click()
    def click_delete_account(self): self.locator_delete_account_button.click()


