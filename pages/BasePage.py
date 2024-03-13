import pytest


class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url="https://automationexercise.com/"):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()
