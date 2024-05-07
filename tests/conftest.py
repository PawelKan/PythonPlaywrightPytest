import json

import pytest
from playwright.sync_api import Page
import os
from pytest_playwright.pytest_playwright import context, playwright

def pytest_addoption(parser):
    parser.addoption("--width", action="store", default=1920, help="Viewport width")
    parser.addoption("--height", action="store", default=1080, help="Viewport height")

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 500,
    }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright, request):
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "auth.json")
    #Need to cast string to int for widht and height
    screen_width = int(request.config.getoption("--width"))
    screen_height = int(request.config.getoption("--height"))

    return {
        **browser_context_args,
        "storage_state": file_path,
        "viewport": {"width": screen_width, "height": screen_height},
    }
