from playwright.sync_api import sync_playwright
import pytest
from resources.variables import URL

@pytest.fixture
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url=URL)
        page.wait_for_load_state('networkidle')
        yield page
        context.close()
        browser.close()