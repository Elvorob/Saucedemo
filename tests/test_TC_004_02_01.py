from ..pages.locators import InventoryPageLocators, CartPageLocators


def test_add_to_cart_check_item(d, correct_login):
    d.find_element(*InventoryPageLocators.RED_TSHIRT_ADD_BTN).click()
    d.find_element(*InventoryPageLocators.CART_BTN).click()
    inv_name = d.find_element(*CartPageLocators.INVENT_ITEM_NAME).text
    assert inv_name == "Test.allTheThings() T-Shirt (Red)", "NOT FOUND"
