import time

import pytest
from faker import Faker
from playwright.sync_api import Page, expect

from data.data_countries import COUNTRY
from pages.login_page import LoginPage
from pages.register_account_success_page import RegisterAccountSuccessPage
from pages.register_page import RegisterPage


class TestRegisterPage:

    @pytest.fixture(autouse = True)
    def before_tests(self, page: Page):
        self.login_page = LoginPage(page)
        self.register_page = RegisterPage(page)
        self.success_page_after_registration = RegisterAccountSuccessPage(page)
        self.login_page.open_page()

    def test_register_new_user(self):
        #Generate data for test:
        fake = Faker()
        name = fake.name()
        email = fake.email()
        day_of_birth = "11"
        month_of_birth = fake.month_name()
        year_of_birth = fake.year()
        first_name = fake.first_name()
        last_name = fake.last_name()
        password = fake.password(length=8)  # Password length can be adjusted
        company = fake.company()
        address1 = fake.street_address()
        address2 = fake.secondary_address()
        country = COUNTRY.CANADA
        city = fake.city()
        state = fake.state()
        zipcode = fake.zipcode()
        mobile_number = fake.phone_number()

        #Go to Login Page and
        self.login_page.fill_sign_up_form(name, email)
        expect(self.register_page.enter_account_information_header_locator).to_be_visible()
        expect(self.register_page.enter_account_information_header_locator).to_have_text("Enter Account Information")

        self.register_page.check_title_mr()
        self.register_page.fill_first_name(first_name)
        self.register_page.fill_last_name(last_name)
        self.register_page.fill_password(password)
        self.register_page.select_day_of_birth(day_of_birth)
        self.register_page.select_month_of_birth(month_of_birth)
        self.register_page.select_year_of_birth(year_of_birth)
        self.register_page.fill_company(company)
        self.register_page.fill_address1(address1)
        self.register_page.fill_address2(address2)
        self.register_page.fill_city(city)
        self.register_page.select_country(country)
        self.register_page.fill_state(state)
        self.register_page.fill_zipcode(zipcode)
        self.register_page.fill_mobile_number(mobile_number)

        self.register_page.click_create_account_btn()

        # ADD ASSERTION FOR CORRECT REGISTRATION
        assert self.success_page_after_registration.get_header_text() == "ACCOUNT CREATED!", "ERROR on Success Page Header text"
        assert self.success_page_after_registration.get_first_paragraph_text() == "Congratulations! Your new account has been successfully created!"
        assert self.success_page_after_registration.get_last_paragraph_text() == "You can now take advantage of member privileges to enhance your online shopping experience with us."
