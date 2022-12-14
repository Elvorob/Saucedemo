from ..pages.locators import InventoryPageLocators
from ..pages.locators import link
from ..pages.login_page import LoginPage


"""TC 005.00.01 -> About page for standard user"""


def test_about_page_standard_user(d):
    page = LoginPage(d, link)
    page.should_be_login_form()
    page.signin_4_username(username="standard_user", password="secret_sauce")
    page.should_go_on_product_page()

    d.find_element(*InventoryPageLocators.BURGER_BTN).click()
    d.implicitly_wait(2)
    d.find_element(*InventoryPageLocators.BURGER_MENU_ABOUT_BTN).click()
    assert d.current_url == "https://saucelabs.com/"
