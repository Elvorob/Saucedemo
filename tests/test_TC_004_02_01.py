from selenium.webdriver.common.by import By
from ..pages.locators import InventoryPageLocators



def test_add_to_cart_check_item(d, correct_login):
    d.find_element(*InventoryPageLocators.RED_TSHIRT_ADD_BTN).click()
    d.find_element(*InventoryPageLocators.CART_BTN).click()
    assert (
        d.find_element(By.CLASS_NAME, "inventory_item_name").text
        == "Test.allTheThings() T-Shirt (Red)"
    ), "NOT FOUND"
