from playwright.sync_api import expect
from pages.home_page import HomePage


def test_NoSuchElementException(setup):
    page = setup

    main_page = HomePage(page)
    main_page.select_Test_Exceptions()

    page.get_by_role("button", name="Add").click()
    expect(page.get_by_text("Row 2 was added")).to_be_visible()
    expect(page.get_by_text("Row 2 Save Edit Remove")).to_be_visible()

def test_ElementNotInteractableException(setup):
    page = setup

    main_page = HomePage(page)
    main_page.select_Test_Exceptions()

    page.get_by_role("button", name="Add").click()
    expect(page.get_by_text("Row 2 was added")).to_be_visible()
    page.get_by_role("textbox").nth(1).click()
    page.get_by_role("textbox").nth(1).fill("Hot Dog")
    page.get_by_role("button", name="Save").click()
    expect(page.get_by_text("Row 2 was saved")).to_be_visible()

def test_InvalidElementStateException(setup):
    page = setup

    main_page = HomePage(page)
    main_page.select_Test_Exceptions()

    page.get_by_role("button", name="Edit").click()
    page.get_by_role("textbox").fill("Hot Dog")
    page.get_by_role("button", name="Save").click()
    expect(page.get_by_text("Row 1 was saved")).to_be_visible()