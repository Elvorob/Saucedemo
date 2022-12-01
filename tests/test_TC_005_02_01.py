# TC_005.02.01 | hamburger menu > All items
# STEPS:
# 1. After authorization, you should be on products list page: https://www.saucedemo.com/inventory.html
# 2. Select any item in the list
# 3. Make left click and open the item page
# 4. On new page click ALL ITEMS in the main menu
# 5. Make sure that you are on products list page: https://www.saucedemo.com/inventory.html again
#
# EXPECTED RESULTS:
# User should see https://www.saucedemo.com/inventory.html page

from ..pages.login_page import *
from ..pages.locators import InventoryPageLocators


def test_hamburger_menu(d):
    page = LoginPage(d, LINK_MAIN)
    page.signin_standart_user(login=USER_NAME_STANDARD, password=PASSWORD)
    assert d.current_url == LINK_INVENTORY
    items = d.find_elements(*InventoryPageLocators.INVENTORY_ITEMS)
    assert len(items) == 6
    items[0].click()
    time.sleep(2)
    assert d.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"
    d.find_element(*InventoryPageLocators.BURGER_BTN).click()
    time.sleep(2)
    d.find_element(*InventoryPageLocators.BURGER_MENU_ALL_ITEMS_BTN).click()
    assert d.current_url == LINK_INVENTORY
