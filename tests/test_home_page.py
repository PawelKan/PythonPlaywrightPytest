import pytest

from pages.HomePage import HomePage


class TestHomePage:

    @pytest.fixture(autouse=True)
    def before_tests(self, setup_browser):
        self.home_page = HomePage(setup_browser)

    def test_home_page(self, setup_browser):
        self.home_page.navigate()
        page_title_actual = self.home_page.get_title()
        assert page_title_actual == "Automation Exercise"

        self.home_page.click_products()
        products_page_title = self.home_page.get_title()
        assert products_page_title == "Automation Exercise - All Products"

        self.home_page.click_cart_button()
        cart_page_title = self.home_page.get_title()
        assert cart_page_title == "Automation Exercise - Checkout"


