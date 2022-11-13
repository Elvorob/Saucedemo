from .pages.locators import InventoryPageLocators
from .pages.locators import InventoryItemPageLocator


def test_compare_item_names(driver, correct_login):
    get_name_list = driver.find_element(*InventoryPageLocators.BIKELIGHT_LABEL).text
    driver.find_element(*InventoryPageLocators.BIKELIGHT_LABEL).click()
    get_name_card = driver.find_element(*InventoryItemPageLocator.INVENTORY_ITMEM_LABEL).text
    assert get_name_list == get_name_card, "Item Name !ARE NOT! the same"


def test_compare_item_desc(driver, correct_login):
    get_name_list = driver.find_element(*InventoryPageLocators.BIKELIGHT_DESCRIPTION).text
    driver.find_element(*InventoryPageLocators.BIKELIGHT_LABEL).click()
    get_name_card = driver.find_element(*InventoryItemPageLocator.INVENTORY_ITMEM_DESCRIPTION).text
    assert get_name_list == get_name_card, "Item description !ARE NOT! the same"


def test_compare_item_price(driver, correct_login):
    get_name_list = driver.find_element(*InventoryPageLocators.BIKELIGHT_PRICE).text
    driver.find_element(*InventoryPageLocators.BIKELIGHT_LABEL).click()
    get_name_card = driver.find_element(*InventoryItemPageLocator.INVENTORY_ITMEM_PRICE).text
    assert get_name_list == get_name_card, "Item Price !ARE NOT! the same"


def test_compare_item_img(driver, correct_login):
    get_name_list = driver.find_element(*InventoryPageLocators.BIKELIGHT_IMG).get_attribute("src")
    driver.find_element(*InventoryPageLocators.BIKELIGHT_LABEL).click()
    get_name_card = driver.find_element(*InventoryItemPageLocator.INVENTORY_ITMEM_IMG).get_attribute("src")
    assert get_name_list == get_name_card, "Item image !ARE NOT! the same"
