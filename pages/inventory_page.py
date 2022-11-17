import time

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

    def add_to_cart_backpack(self):
        self.d.find_element(*InventoryPageLocators.BACKPACK_ADD_BTN).click()

    def item_added_to_cart(self):
        assert self.element_is_present(*InventoryPageLocators.CART_BADGE)
        assert self.element_is_present(*InventoryPageLocators.BACKPACK_REMOVE_BTN)

    def no_item_in_cart(self):
        assert self.element_is_NOT_present(*InventoryPageLocators.CART_BADGE)
        assert self.element_is_NOT_present(*InventoryPageLocators.BACKPACK_REMOVE_BTN)

    def remove_backpack_from_cart(self):
        self.d.find_element(*InventoryPageLocators.BACKPACK_REMOVE_BTN).click()

    def user_on_inventory_page(self):
        assert "inventory" in self.d.current_url

    def sort_items_on_inventory_page_az(self):
        unsortedlist = self.d.find_elements(By.CSS_SELECTOR, ".inventory_item_name")
        self.d.find_element(*InventoryPageLocators.SORT_MENU_BUTTON).click()
        time.sleep(2)
        self.d.find_element(*InventoryPageLocators.SORT_OPTION_BUTTON_AZ).click()
        time.sleep(2)
        sortedlistAZ = self.d.find_elements(By.CSS_SELECTOR, ".inventory_item_name")
        assert sortedlistAZ[0] == unsortedlist[0]

    def sort_items_on_inventory_page_za(self):
        self.d.find_element(*InventoryPageLocators.SORT_MENU_BUTTON).click()
        time.sleep(2)
        self.d.find_element(*InventoryPageLocators.SORT_OPTION_BUTTON_AZ).click()
        time.sleep(2)
        sortedlistAZ = self.d.find_elements(By.CSS_SELECTOR, ".inventory_item_name")
        self.d.find_element(*InventoryPageLocators.SORT_MENU_BUTTON).click()
        time.sleep(2)
        self.d.find_element(*InventoryPageLocators.SORT_OPTION_BUTTON_ZA).click()
        time.sleep(2)
        sortedlistZA = self.d.find_elements(By.CSS_SELECTOR, ".inventory_item_name")
        assert sortedlistZA[0] == sortedlistAZ[-1]

    def sort_items_on_inventory_page_lowhigh_highlow(self):
        self.d.find_element(*InventoryPageLocators.SORT_MENU_BUTTON).click()
        self.d.find_element(*InventoryPageLocators. SORT_OPTION_BUTTON_LOWHIGH).click()
        time.sleep(2)
        sortedlist = self.d.find_elements(By.CSS_SELECTOR, ".inventory_item_price")
        self.d.find_element(*InventoryPageLocators.SORT_MENU_BUTTON).click()
        self.d.find_element(*InventoryPageLocators.SORT_OPTION_BUTTON_HIGHLOW).click()
        time.sleep(2)
        sortedlist1 = self.d.find_elements(By.CSS_SELECTOR, ".inventory_item_price")
        assert sortedlist[0] == sortedlist1[-1]


