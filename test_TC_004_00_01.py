from pages.locators import *


def test_open_cart(driver, correct_login):
    assert driver.title == "Swag Labs", "NOT ENTER"
    driver.find_element(*InventoryPageLocators.CART_BTN).click()
    assert driver.current_url == "https://www.saucedemo.com/cart.html"
    driver.find_element(*CartPageLocators.CONTINUE_SHOPPING).click()
    assert driver.title == "Swag Labs", "____You NOT LEFT_____"
    driver.quit()
