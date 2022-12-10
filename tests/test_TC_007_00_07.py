from ..pages.locators import InventoryPageLocators, CartPageLocators, CheckoutPageLocators


def test_check_if_form_empty(d, correct_login):
    d.find_element(*InventoryPageLocators.FLEECE_JACKET_ADD_BTN).click()
    d.find_element(*InventoryPageLocators.CART_BTN).click()
    d.find_element(*CartPageLocators.BT_CHECKOUT).click()
    d.find_element(*CheckoutPageLocators.CONTINUE).click()
    d.find_element(*CheckoutPageLocators.ERROR_MSG).is_displayed(), "Message error not founded"
