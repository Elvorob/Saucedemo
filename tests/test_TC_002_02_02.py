import pytest
from ..pages.locators import InventoryPageLocators
from ..pages.login_page import LoginPage
from ..pages.locators import link
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


@pytest.mark.xfail
def test_product_cart_new_window(d):
    page = LoginPage(d, link)
    page.signin_4_username(username="problem_user", password="secret_sauce")
    page.should_go_on_product_page()
    d.maximize_window()
    achains = ActionChains(d)
    backpack = d.find_element(*InventoryPageLocators.BACKPACK_LINK).click()
    # make right click
    achains.context_click(backpack).perform()
    d.implicitly_wait(1)
    # choose in context menu "open in new window"
    achains.context_click(backpack).send_keys(Keys.ARROW_DOWN).send_keys(
        Keys.RETURN
    ).perform()
    assert d.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"
