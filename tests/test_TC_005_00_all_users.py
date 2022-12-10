import pytest
from ..pages.locators import InventoryPageLocators



@pytest.mark.xfail
def test_about_page_all_users(d, login_from_list):
    d.find_element(*InventoryPageLocators.BURGER_BTN).click()
    d.implicitly_wait(30)
    d.find_element(*InventoryPageLocators.BURGER_MENU_ABOUT_BTN).click()
    assert d.current_url == "https://saucelabs.com/"
