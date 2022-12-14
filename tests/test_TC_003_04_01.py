from ..pages.locators import InventoryPageLocators, CartPageLocators


def test_check_item_info(d, correct_login):
    d.find_element(*InventoryPageLocators.FLEECE_JACKET_ADD_BTN).click()
    d.find_element(*InventoryPageLocators.CART_BTN).click()
    d.find_element(*CartPageLocators.INVENT_ITEM_NAME).is_displayed()
    d.find_element(*CartPageLocators.INVENT_ITEM_DESC).is_displayed()
    d.find_element(*CartPageLocators.INVENT_ITEM_PRICE).is_displayed()
