import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..pages.locators import InventoryPageLocators, CartPageLocators

MENU_RESET = (By.ID, "reset_sidebar_link")


@pytest.mark.xfail(reason="_BUG_: NotRese Page only cart")
def test_reset_app(d, correct_login):
    d.find_element(*InventoryPageLocators.BACKPACK_ADD_BTN).click()
    d.find_element(*InventoryPageLocators.BURGER_BTN).click()
    wait = WebDriverWait(d, 10)
    cross_btn = wait.until(EC.element_to_be_clickable(MENU_RESET))
    cross_btn.click()
    a = d.find_element(*CartPageLocators.REMOVE_ITEM_BTN).text
    assert (a == "ADD TO CART"), "NOT RESET"
