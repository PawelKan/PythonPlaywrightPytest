

class TestHomePage:
    def test_home_page(self, setup_browser):
        self.page = setup_browser
        self.page.goto("https://automationexercise.com/")
