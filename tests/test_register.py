import allure
import pytest
from faker import Faker
from playwright.sync_api import Page, expect
from data.data_countries import COUNTRY
from pages.page_manager import PageManager
from data.user_data_test_generator import UserDataTestGenerator

class TestRegisterPage:

    @pytest.fixture(autouse=True)
    def before_tests(self, page: Page):
        self.pm = PageManager(page)
        self.pm.on_login_page().open_page()

    @pytest.mark.functional
    def test_register_new_user(self):
        random_user_data = UserDataTestGenerator.get_random_user_data()
        #Go to Login Page and
        self.pm.on_login_page().fill_sign_up_form(random_user_data["name"], random_user_data["email"])
        expect(self.pm.on_register_page().enter_account_information_header_locator).to_be_visible()
        expect(self.pm.on_register_page().enter_account_information_header_locator).to_have_text("Enter Account Information")

        self.pm.on_register_page().check_title_mr()
        self.pm.on_register_page().fill_first_name(random_user_data["first_name"])
        self.pm.on_register_page().fill_last_name(random_user_data["last_name"])
        self.pm.on_register_page().fill_password(random_user_data["password"])
        self.pm.on_register_page().select_day_of_birth(random_user_data["day_of_birth"])
        self.pm.on_register_page().select_month_of_birth(random_user_data["month_of_birth"])
        self.pm.on_register_page().select_year_of_birth(random_user_data["year_of_birth"])
        self.pm.on_register_page().fill_company(random_user_data["company"])
        self.pm.on_register_page().fill_address1(random_user_data["address1"])
        self.pm.on_register_page().fill_address2(random_user_data["address2"])
        self.pm.on_register_page().fill_city(random_user_data["city"])
        self.pm.on_register_page().select_country(random_user_data["country"])
        self.pm.on_register_page().fill_state(random_user_data["state"])
        self.pm.on_register_page().fill_zipcode(random_user_data["zipcode"])
        self.pm.on_register_page().fill_mobile_number(random_user_data["mobile_number"])

        self.pm.on_register_page().click_create_account_btn()

        # ADD ASSERTION FOR CORRECT REGISTRATION
        assert self.pm.on_success_page_after_registration().get_header_text() == "ACCOUNT CREATED!", "ERROR on Success Page Header text"
        assert self.pm.on_success_page_after_registration().get_first_paragraph_text() == "Congratulations! Your new account has been successfully created!"
        assert self.pm.on_success_page_after_registration().get_last_paragraph_text() == "You can now take advantage of member privileges to enhance your online shopping experience with us."

