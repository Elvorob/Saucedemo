from ..pages.locators import InventoryPageLocators
from ..pages.login_page import LoginPage
from ..pages.locators import link
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def test_product_cart_new_window(d):
    page = LoginPage(d, link)
    page.signin_4_username(username="performance_glitch_user", password="secret_sauce")
    page.should_go_on_product_page()

    achains = ActionChains(d)
    backpack = d.find_element(*InventoryPageLocators.BACKPACK_LINK).click()
    achains.context_click(backpack).perform()
    d.implicitly_wait(2)
    achains.context_click(backpack).send_keys(Keys.ARROW_DOWN).send_keys(
        Keys.RETURN
    ).perform()
    assert d.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"
