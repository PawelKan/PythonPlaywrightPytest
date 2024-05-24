from playwright.sync_api import Page

from data.data_countries import COUNTRY
from tests.test_automationexercise_pom.pages.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.register_fields_section = page.locator(".login-form")
        self.enter_account_information_header_locator = page.locator(f'.login-form .title:has-text("Enter Account Information")')
        self.title_mr_rad_locator = page.locator("#id_gender1")
        self.title_mrs_rad_locator = page.locator("#id_gender2")
        self.name_txt_locator = page.locator("[data-qa=\"name\"]")
        self.email_txt_locator = page.locator("[data-qa=\"email\"]")
        self.pass_txt_locator = page.locator("[data-qa=\"password\"]")

        self.date_of_birth_day_list_locator = page.locator("[data-qa=\"days\"]")
        self.date_of_birth_month_list_locator = page.locator("[data-qa=\"months\"]")
        self.date_of_birth_year_list_locator = page.locator("[data-qa=\"years\"]")

        self.newsletter_chk_locator = page.locator("#form > div > div > div > div > form > div:nth-child(7)")
        self.special_offers_chk_locator = page.locator("#optin")

        self.first_name_txt_locator = page.locator("[data-qa=\"first_name\"]")
        self.last_name_txt_locator = page.locator("[data-qa=\"last_name\"]")
        self.company_txt_locator = page.locator("[data-qa=\"company\"]")
        self.address1_txt_locator = page.locator("[data-qa=\"address\"]")
        self.address2_txt_locator = page.locator("[data-qa=\"address2\"]")
        self.country_list_locator = page.locator("[data-qa=\"country\"]")
        self.state_txt_locator = page.locator("[data-qa=\"state\"]")
        self.city_txt_locator = page.locator("[data-qa=\"city\"]")
        self.zipcode_txt_locator = page.locator("[data-qa=\"zipcode\"]")
        self.mobile_number_txt_locator = page.locator("[data-qa=\"mobile_number\"]")
        self.create_account_btn_locator = page.locator("[data-qa=\"create-account\"]")
        self.all_labels_on_page = page.locator("label")

    def check_title_mr(self):
        self.title_mr_rad_locator.check()
    def check_title_mrs(self):
        self.title_mrs_rad_locator.check()
    def fill_name(self, text):
        self.name_txt_locator.fill(text)
    def fill_email(self, text):
        self.email_txt_locator.fill(text)
    def fill_password(self, text):
        self.pass_txt_locator.fill(text)

    def select_day_of_birth(self, text):
        self.date_of_birth_day_list_locator.select_option(text)
    def select_month_of_birth(self, text):
        self.date_of_birth_month_list_locator.select_option(text)
    def select_year_of_birth(self, text):
        self.date_of_birth_year_list_locator.select_option(text)
    def fill_first_name(self, text):
        self.first_name_txt_locator.fill(text)
    def fill_last_name(self, text):
        self.last_name_txt_locator.fill(text)
    def fill_company(self, text):
        self.company_txt_locator.fill(text)

    def fill_address1(self, text):
        self.address1_txt_locator.fill(text)

    def fill_address2(self, text):
        self.address2_txt_locator.fill(text)

    def select_country(self, country: COUNTRY):
        self.country_list_locator.select_option(country.value)

    def fill_state(self, text):
        self.state_txt_locator.fill(text)

    def fill_city(self, text):
        self.city_txt_locator.fill(text)

    def fill_zipcode(self, text):
        self.zipcode_txt_locator.fill(text)

    def fill_mobile_number(self, text):
        self.mobile_number_txt_locator.fill(text)

    def click_create_account_btn(self):
        self.create_account_btn_locator.click()