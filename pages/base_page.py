from selenium.common.exceptions import NoSuchElementException
from .locators import *


class BasePage():

    def __init__(self, d, link):
        self.d = d
        self.link = link

    def open_page(self):
        self.d.get(self.link)

    def element_is_present(self, method, locator):
        try:
            self.d.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    def should_be_autorized_user(self):
        assert self.element_is_present(*InventoryPageLocators.CART_BTN)

    def element_is_NOT_present(self, method, locator):
        try:
            self.d.find_element(method, locator)
        except NoSuchElementException:
            return True
        return False
