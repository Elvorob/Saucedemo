from ..pages.locators import InventoryPageLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def test_product_cart_new_page(d, correct_login):
    d.maximize_window()
    achains = ActionChains(d)
    backpack = d.find_element(*InventoryPageLocators.BACKPACK_LINK).click()
    achains.context_click(backpack).perform()
    d.implicitly_wait(1)
    achains.context_click(backpack).send_keys(Keys.ARROW_DOWN).send_keys(
        Keys.RETURN
    ).perform()
    assert d.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"
