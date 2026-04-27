from playwright.sync_api import expect
from pages.home_page import HomePage


def test_NoSuchElementException(setup):
    page = setup

    main_page = HomePage(page)
    main_page.select_Test_Exceptions()

    page.get_by_role("button", name="Add").click()
    expect(page.get_by_text("Row 2 was added")).to_be_visible()
    expect(page.get_by_text("Row 2 Save Edit Remove")).to_be_visible()
