import pytest
from ..pages.cart_page import CartPage
from ..pages.locators import InventoryPageLocators, link, CartPageLocators


@pytest.mark.xfail(reason="NotWorking_BUG,not implemented")
def test_change_qty_plus(d, correct_login):
    d.find_element(*InventoryPageLocators.RED_TSHIRT_ADD_BTN).click()
    cart = CartPage(d, link)
    cart.click_icon_cart()
    d.find_element(*CartPageLocators.CART_QUANTITY).click()


@pytest.mark.xfail(reason="NotWorking_BUG,not implemented")
def test_change_qty_minus(d, correct_login):
    d.find_element(*InventoryPageLocators.RED_TSHIRT_ADD_BTN).click()
    cart = CartPage(d, link)
    cart.click_icon_cart()
    d.find_element(*CartPageLocators.CART_QUANTITY).click()
