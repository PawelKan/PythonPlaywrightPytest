import os

import pytest
from playwright.sync_api import Page
from playwright.sync_api import expect


class TestDemoQAPage:
    """Tests written without Page Object Pattern for Playwright learning purposes"""
    @pytest.fixture(autouse=True, scope="function")
    def before_tests_fixture(self, page: Page):
        """Open page and click on Elements before each test"""
        self.page = page
        page.goto("https://demoqa.com/")
        self.page.get_by_text("Elements").click()


    def test_radio_buttons(self):
        """Test NOT genereted with codegen tool"""
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

    def tests_buttons(self):
        self.page.locator('.menu-list .btn-light#item-4').first.click()
        # double click
        # right click
        # Click Me
        self.page.locator('text="Click Me"').click()
        expect(self.page.locator("#dynamicClickMessage")).to_contain_text("You have done a dynamic click")

        self.page.locator("#doubleClickBtn").dblclick()
        expect(self.page.locator("#doubleClickMessage")).to_contain_text("You have done a double click")

        self.page.locator("#rightClickBtn").click(button="right")
        expect(self.page.locator("#rightClickMessage")).to_contain_text("You have done a right click")

    def test_upload_and_download_file(self) -> None:
        """Go to Upload and Download page and upload and download file"""
        file_path = os.path.join(os.getcwd(), "tests", "data", "EmptyFileForUploadTest.txt")

        self.page.get_by_text("Upload and Download").click()

        #Download file
        with self.page.expect_download() as download_info:
            self.page.get_by_role("link", name="Download").click()
        download = download_info.value
        print(download)

        #Upload file
        self.page.get_by_label("Select a file").set_input_files(file_path)

        #Check message after file upload
        expect(self.page.get_by_text("C:\\fakepath\\EmptyFileForUploadTest.txt")).to_be_visible()

    def test_forms_practice_forms(self):
        self.page.get_by_text("Forms").click()
        self.page.get_by_text("Practice Form").click()

        self.page.get_by_placeholder("First Name").fill("testFirstName")
        self.page.get_by_placeholder("Last Name").fill("testLastName")
        self.page.get_by_placeholder(f'name@example.com').fill("testMail@testmailexercisenotavailable.pl")
        self.page.locator('[for=\'gender-radio-1\']').click() #click on male radio button
        self.page.get_by_placeholder("Mobile Number").fill("1234567890")

        #select date of birth
        self.page.locator("#dateOfBirthInput").click()
        self.page.get_by_role("button", name="Next Month", exact=True).click()
        self.page.locator('[role="option"]').filter(has_text="17").first.click()

        #Subject
        self.page.locator("#subjectsInput").fill("Math")
        self.page.get_by_text("Maths", exact=True).click()

        self.page.get_by_text("Sports").click()
        self.page.get_by_placeholder("Current Address").fill("testCurrentAddress")

        #Select Stage
        self.page.locator("#stateCity-wrapper").filter(has_text="Select State").click()
        self.page.get_by_text("NCR", exact=True).click()
        #Select City
        self.page.locator("#stateCity-wrapper").get_by_text("Select City", exact=True).click()
        self.page.get_by_text("Delhi", exact=True).click()
        #Submit form
        self.page.get_by_role("button", name="Submit").click()

        expect(self.page.locator(".modal-content")).to_be_visible()
        expect(self.page.locator(".modal-content").filter(has_text="Thanks for submitting the form")).to_be_visible()
        expect(self.page.locator(".modal-content.modal-content tr th").first).to_contain_text("Label")
        expect(self.page.locator(".modal-content.modal-content tr th").last).to_contain_text("Values")

        expect(self.page.locator(".modal-content.modal-content").get_by_role("cell", name="Student Name")).to_be_visible()
        expect(self.page.locator(".modal-content.modal-content").get_by_role("cell", name="Student Email")).to_be_visible()
        expect(self.page.locator(".modal-content.modal-content").get_by_role("cell", name="Gender")).to_be_visible()
        expect(self.page.locator(".modal-content.modal-content").get_by_role("cell", name="Mobile")).to_be_visible()
        expect(self.page.locator(".modal-content.modal-content").get_by_role("cell", name="Date of Birth")).to_be_visible()
        expect(self.page.locator(".modal-content.modal-content").get_by_role("cell", name="Subjects")).to_be_visible()
        expect(self.page.locator(".modal-content.modal-content").get_by_role("cell", name="Hobbies")).to_be_visible()
        expect(self.page.locator(".modal-content.modal-content").get_by_role("cell", name="Picture")).to_be_visible()
        expect(self.page.locator(".modal-content.modal-content").get_by_role("cell", name="Address").first).to_be_visible()
        expect(self.page.locator(".modal-content.modal-content").get_by_role("cell", name="State and City")).to_be_visible()