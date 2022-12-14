import pytest
from ..pages.locators import InventoryPageLocators
from ..pages.locators import link
from ..pages.login_page import LoginPage


"""TC 005.03.00 -> All users can logout"""
@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
    ],
)
def test_logout(d, username, password):
    page = LoginPage(d, link)
    page.should_be_login_form()
    page.signin_4_username(username, password)
    d.implicitly_wait(2)
    page.should_go_on_product_page()

    d.find_element(*InventoryPageLocators.BURGER_BTN).click()
    d.implicitly_wait(2)
    d.find_element(*InventoryPageLocators.BURGER_MENU_LOGOUT_BTN).click()
    assert d.current_url == link
