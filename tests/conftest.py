import json

import pytest
from playwright.sync_api import Page
import os

from pytest_playwright.pytest_playwright import context, playwright

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 500,
    }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "auth.json")

    return {
        **browser_context_args,
        "storage_state": file_path
    }
