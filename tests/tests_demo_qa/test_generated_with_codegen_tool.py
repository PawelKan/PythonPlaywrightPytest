import pytest
from playwright.sync_api import Page, expect


class TestDemoQAPageWithCodegen:
    @pytest.fixture(autouse=True, scope="function")
    def before_tests_fixture(self, page: Page):
        self.page = page
        page.goto("https://demoqa.com/")
    @pytest.mark.codegen
    def test_example_with_codegen(self, page:Page):
        """Tests created with codegen (exercise)"""
        """Fill text form and assert text at the end"""
        self.page.locator("svg").first.click()
        self.page.locator("li").filter(has_text="Text Box").click()
        self.page.get_by_placeholder("Full Name").click()
        self.page.get_by_placeholder("Full Name").fill("FullNameText")
        self.page.get_by_placeholder("Full Name").press("Tab")
        self.page.get_by_placeholder("name@example.com").fill("email@testmail.com")
        self.page.get_by_placeholder("name@example.com").press("Tab")
        self.page.get_by_placeholder("Current Address").fill("CurrentAddressTextg")
        self.page.get_by_placeholder("Current Address").press("Tab")
        self.page.locator("#permanentAddress").fill("PermanentAddressText")
        self.page.get_by_role("button", name="Submit").click()
        expect(page.locator("#name")).to_contain_text("Name:FullNameText")
        expect(page.locator("#email")).to_contain_text("Email:email@testmail.com")
        expect(page.locator("#output")).to_contain_text("Current Address :CurrentAddressTextg")
        expect(page.locator("#output")).to_contain_text("Permananet Address :PermanentAddressText")

    @pytest.mark.codegen
    def test_checkboxes_with_codegen(self, page: Page, context):
        """Tests created with codegen (exercise)"""
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        self.page.locator("path").first.click()
        self.page.locator("li").filter(has_text="Check Box").click()
        self.page.locator("#tree-node").get_by_role("img").nth(3).click()
        expect(page.locator("#result")).to_contain_text(
            "You have selected :homedesktopnotescommandsdocumentsworkspacereactangularveuofficepublicprivateclassifiedgeneraldownloadswordFileexcelFile")
        self.page.get_by_label("Expand all").click()
        expect(page.locator("#tree-node")).to_contain_text("Excel File.doc")
        self.page.get_by_label("Collapse all").click()
        expect(page.locator("ol")).to_contain_text("Home")
        expect(page.locator("#tree-node").filter(has_text="Excel File.doc")).not_to_be_visible()
        context.tracing.stop(path="test_checkboxes_with_codegen.zip")