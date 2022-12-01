# TC_007.01.01 | Checkout: Your information > Verify that you can cancel the checkout process
# Environment:
# Web Version
#
# Test Data
# Username: standard_user
# Password: secret_sauce
#
# PRECONDITIONS:
# 1. Log in to Swag Labs
# 2. Enter the page https://www.saucedemo.com/inventory.html
#
# Steps:
#
# Add 1-3 products in a cart.
# Click on a Cart icon
# Check that all chosen items are in a cart.
# Click Checkout button.
# Click Cancel button.
# Expected result: When you click Cancel button, you're switching to the previous page with the list of chosen items.

from ..pages.login_page import *
from ..pages.locators import (
    CartPageLocators,
    CheckoutPageLocators,
    InventoryPageLocators,
)


def test_cancel_checkout(d):
    page = LoginPage(d, LINK_MAIN)
    page.signin_standart_user(login=USER_NAME_STANDARD, password=PASSWORD)
    assert d.current_url == LINK_INVENTORY
    d.find_element(*InventoryPageLocators.BACKPACK_ADD_BTN).click()
    d.find_element(*InventoryPageLocators.BOLT_TSHIRT_ADD_BTN).click()
    d.find_element(*InventoryPageLocators.ONESIE_ADD_BTN).click()
    d.find_element(*InventoryPageLocators.CART_BTN).click()
    time.sleep(2)
    assert d.current_url == LINK_CART
    items = d.find_elements(*InventoryPageLocators.INVENTORY_ITEMS)
    assert len(items) == 3
    d.find_element(*CartPageLocators.BT_CHECKOUT).click()
    time.sleep(2)
    assert d.current_url == LINK_CHECKOUT_STEP_ONE
    d.find_element(*CheckoutPageLocators.CANCEL).click()
    time.sleep(2)
    assert d.current_url == LINK_CART
