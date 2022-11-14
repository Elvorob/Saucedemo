from .locators import *
from .base_page import *


class CartPage(BasePage):
    def backpack_can_be_removed(self):
        self.d.find_element(*CartPageLocators.REMOVE_ITEM_BTN).click()

    def cart_is_empty(self):
        assert self.element_is_NOT_present(*CartPageLocators.CART_ITEM_BLOCK)

    def click_icon_cart(self):
        self.d.find_element(*CartPageLocators.CART_ICON).click()
