from ..pages.locators import InventoryPageLocators, CartPageLocators


def test_open_cart(d, correct_login):
    assert d.title == "Swag Labs", "NOT ENTER"
    d.find_element(*InventoryPageLocators.CART_BTN).click()
    assert d.current_url == CartPageLocators.LINK_CART
    d.find_element(*CartPageLocators.CONTINUE_SHOPPING).click()
    assert d.title == "Swag Labs", "____You NOT LEFT_____"
