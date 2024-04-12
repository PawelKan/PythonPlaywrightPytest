import json

import pytest
from playwright.sync_api import Page
import os

from pytest_playwright.pytest_playwright import context

"""Before test add cookies, because popup Consent page was randomly displayed on page"""
# @pytest.fixture(autouse=True, scope="session")
# def browser_type_launch_args(browser_type_launch_args):
#     return {
#         **browser_type_launch_args,
#         "headless"
#     }

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 500
    }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    # Ustaw argumenty kontekstu przeglądarki, aby ustawić stan magazynu sesji
    return {
        **browser_context_args,
        "storage_state": 'data\\auth.json',
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
}
