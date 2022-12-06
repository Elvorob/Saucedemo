import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from ..pages.login_page import *
from ..pages.inventory_page import *
from ..pages.locators import *


def test_sort_items_az_za_lowhigh_highlow_all_users(d, login_from_list):
    page = InventoryPage(d, link)
    page.sort_items_on_inventory_page_az_za()
    page.sort_items_on_inventory_page_lowhigh_highlow()


def test_product_cart_new_page(d, login_from_list):
    d.maximize_window()
    achains = ActionChains(d)
    backpack = d.find_element(*InventoryPageLocators.BACKPACK_LINK).click()
    achains.context_click(backpack).perform()
    d.implicitly_wait(1)
    achains.context_click(backpack).send_keys(Keys.ARROW_DOWN).send_keys(
        Keys.RETURN
    ).perform()
    assert d.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"


def test_return_from_itempage(d, login_from_list):
    page = InventoryPage(d, link)
    page.go_to_backpack_item_page()
    page.go_back_from_itempage_to_inventorypage()


def test_remove_item_from_the_cart(d, correct_login):
    page = InventoryPage(d, link)
    page.no_item_in_cart()
    page.add_to_cart_backpack()
    page.item_added_to_cart()
    page.remove_backpack_from_cart()
    page.no_item_in_cart()


def test_compare_item_names(d, correct_login):
    get_name_list = d.find_element(*InventoryPageLocators.BIKELIGHT_LABEL).text
    d.find_element(*InventoryPageLocators.BIKELIGHT_LABEL).click()
    get_name_card = d.find_element(*InventoryItemPageLocator.INVENTORY_ITMEM_LABEL).text
    assert get_name_list == get_name_card, "Item Name !ARE NOT! the same"


def test_compare_item_desc(d, correct_login):
    get_desc_list = d.find_element(*InventoryPageLocators.BIKELIGHT_DESCRIPTION).text
    d.find_element(*InventoryPageLocators.BIKELIGHT_LABEL).click()
    get_desc_card = d.find_element(
        *InventoryItemPageLocator.INVENTORY_ITMEM_DESCRIPTION
    ).text
    assert get_desc_list == get_desc_card, "Item description !ARE NOT! the same"


def test_compare_item_price(d, correct_login):
    get_price_list = d.find_element(*InventoryPageLocators.BIKELIGHT_PRICE).text
    d.find_element(*InventoryPageLocators.BIKELIGHT_LABEL).click()
    get_price_card = d.find_element(
        *InventoryItemPageLocator.INVENTORY_ITMEM_PRICE
    ).text
    assert get_price_list == get_price_card, "Item Price !ARE NOT! the same"


def test_compare_item_img(d, correct_login):
    get_img_list = d.find_element(*InventoryPageLocators.BIKELIGHT_IMG).get_attribute(
        "src"
    )
    d.find_element(*InventoryPageLocators.BIKELIGHT_LABEL).click()
    get_img_card = d.find_element(
        *InventoryItemPageLocator.INVENTORY_ITMEM_IMG
    ).get_attribute("src")
    assert get_img_list == get_img_card, "Item image !ARE NOT! the same"


def test_check_item_info(d, correct_login):
    d.find_element(*InventoryPageLocators.FLEECE_JACKET_ADD_BTN).click()
    d.find_element(*InventoryPageLocators.CART_BTN).click()
    d.find_element(By.CLASS_NAME, "inventory_item_name").is_displayed()
    d.find_element(By.CLASS_NAME, "inventory_item_desc").is_displayed()
    d.find_element(By.CLASS_NAME, "inventory_item_price").is_displayed()
