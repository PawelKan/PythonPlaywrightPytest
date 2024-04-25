import pytest
from playwright.sync_api import Page
from playwright.sync_api import expect


class TestDemoQAPage:
    @pytest.fixture(autouse=True, scope="function")
    def before_tests_fixture(self, page: Page):
        self.page = page
        page.goto("https://demoqa.com/")

    """tests written without Page Object Pattern for playwright learning purposes"""
    def test_radio_buttons(self):
        """Test NOT genereted with codegen tool"""
        self.page.get_by_text("Elements").click()
        self.page.get_by_text("Radio Button").click()

        #Verify Yes radio button
        expect(self.page.locator(".mt-3")).not_to_be_visible() # information is not visible
        self.page.get_by_text("Yes").check()
        expect(self.page.locator(".mt-3")).to_contain_text("You have selected Yes")

        # Verify Impressive radio button and message
        self.page.get_by_text("Impressive").check()
        expect(self.page.locator(".mt-3")).to_contain_text("You have selected Impressive")

        # Verify No radio button
        expect(self.page.get_by_role("radio", name="no")).to_be_disabled()

    def test_web_tables(self):
        #Open Web Tables page
        self.page.get_by_text("Elements").click()
        self.page.get_by_text("Web Tables").click()
        # Verify column headers names
        expect(self.page.get_by_role('row').first).to_contain_text("First Name")
        expect(self.page.get_by_role('row').first).to_contain_text("Last Name")
        expect(self.page.get_by_role('row').first).to_contain_text("Age")
        expect(self.page.get_by_role('row').first).to_contain_text("Email")
        expect(self.page.get_by_role('row').first).to_contain_text("Salary")
        expect(self.page.get_by_role('row').first).to_contain_text("Department")
        expect(self.page.get_by_role('row').first).to_contain_text("Action")

        #click Add Button and add new user to the table
        self.page.locator("#addNewRecordButton").click()
        self.page.get_by_placeholder("First Name").fill("testFirstName")
        self.page.get_by_placeholder("Last Name").fill("testLastName")
        self.page.get_by_placeholder("name@example.com").fill("testMail@testmailexercisenotavailable.pl")
        self.page.get_by_placeholder("Age").fill("20")
        self.page.get_by_placeholder("Salary").fill("3300")
        self.page.get_by_placeholder("Department").fill("testDepartment")
        self.page.get_by_role("button").get_by_text("Submit").click()

        #search new user,
        self.page.get_by_placeholder("Type to search").fill("testMail@testmailexercisenotavailable.pl")
        self.page.locator(".input-group-append").click()
        #...and verify it's visibility in table

        expect(self.page.locator(f'.rt-tbody [role="row"]').first).to_contain_text("testFirstName")
        expect(self.page.locator(f'.rt-tbody [role="row"]').first).to_contain_text("testLastName")
        expect(self.page.locator(f'.rt-tbody [role="row"]').first).to_contain_text("testMail@testmailexercisenotavailable.pl")
        expect(self.page.locator(f'.rt-tbody [role="row"]').first).to_contain_text("20")
        expect(self.page.locator(f'.rt-tbody [role="row"]').first).to_contain_text("3300")
        expect(self.page.locator(f'.rt-tbody [role="row"]').first).to_contain_text("testDepartment")





