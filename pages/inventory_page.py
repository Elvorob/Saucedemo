from .base_page import BasePage
from .locators import *

class InventoryPage(BasePage):
    def add_to_cart_backpack_inventory_item(self):
        self.d.find_element(*InventoryPageLocators.BACKPACK_ADD_BTN).click()
        assert "id=4" in self.d.current_url

    def add_to_cart_backpack_inventory(self):
        self.d.find_element(*InventoryPageLocators.BACKPACK_ADD_BTN).click()
        self.d.find_element(*InventoryPageLocators.CART_BTN).click()
        assert "cart" in self.d.current_url
        assert (
            "Sauce Labs Backpack"
            in self.d.find_element(*InventoryPageLocators.BACKPACK_LABEL).text
        )

    def change_quantity_in_cart(self):
        self.add_to_cart_backpack_inventory()

