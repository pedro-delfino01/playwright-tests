from playwright.sync_api import expect
from pages.home_page import HomePage


def test_LanguageFilter_Java(setup):
    page = setup

    main_page = HomePage(page)
    main_page.select_Test_Table()

    tabela = page.locator("//table[@id='courses_table']/tbody/tr")

    for i in (tabela.count()):
        linha = tabela.child(i)
        