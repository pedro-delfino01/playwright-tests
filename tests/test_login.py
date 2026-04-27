from playwright.sync_api import expect
from pages.home_page import HomePage


def test_PositiveLogIn(setup):
    page = setup

    main_page = HomePage(page)
    main_page.select_Test_Login_Page()

    page.get_by_role("textbox", name="Username").fill("student")
    page.get_by_role("textbox", name="Password").fill("Password123")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_role("heading")).to_contain_text("Logged In Successfully")
    expect(page.get_by_role("strong")).to_contain_text("Congratulations student. You successfully logged in!")
    expect(page.get_by_role("link", name="Log out")).to_be_visible()
    page.get_by_role("link", name="Log out").click()
    expect(page.get_by_role("heading", name="Test login")).to_be_visible()

def test_NegativeUsernameTest(setup):
    page = setup

    main_page = HomePage(page)
    main_page.select_Test_Login_Page()

    page.get_by_role("textbox", name="Username").fill("incorrectUser")
    page.get_by_role("textbox", name="Password").fill("Password123")
    page.get_by_role("button", name="Submit").click()
    expect(page.locator("#error")).to_contain_text("Your username is invalid!")

def test_NegativePasswordTest(setup):
    page = setup

    main_page = HomePage(page)
    main_page.select_Test_Login_Page()

    page.get_by_role("textbox", name="Username").fill("student")
    page.get_by_role("textbox", name="Password").fill("incorrectPassword")
    page.get_by_role("button", name="Submit").click()
    expect(page.locator("#error")).to_contain_text("Your password is invalid!")



