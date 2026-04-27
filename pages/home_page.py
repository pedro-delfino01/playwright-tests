from playwright.sync_api import Page, expect

class HomePage():
    def __init__(self, page):
        self.page = page

    def select_Test_Login_Page(self):
        self.page.get_by_role("link", name="Test Login Page").click()
        expect(self.page.locator("h2")).to_contain_text("Test login")

    def select_Test_Exceptions(self):
        self.page.get_by_role("link", name="Test Exceptions").click()
        expect(self.page.locator("h2")).to_contain_text("Test Exceptions")

    def select_Test_Table(self):
        self.page.get_by_role("link", name="Test Table").click()
        expect(self.page.locator("h2")).to_contain_text("Test Table")
