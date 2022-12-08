import pytest
from ..pages.locators import link
from ..pages.login_page import LoginPage
from ..pages.locators import InventoryPageLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


@pytest.mark.parametrize(
    "username, password",
    [
        ("standard_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
        pytest.param(
            ("problem_user", "secret_sauce"),
            ("locked_out_user", "secret_sauce"),
            marks=pytest.mark.xfail(raises=AssertionError),
        ),
    ],
)
def test_product_cart_new_window(d, username, password):
    page = LoginPage(d, link)
    page.signin_4_username(username, password)
    page.should_go_on_product_page()
    d.maximize_window()
    achains = ActionChains(d)
    # choose an item
    backpack = d.find_element(*InventoryPageLocators.BACKPACK_LINK).click()
    # right click
    achains.context_click(backpack).perform()
    d.implicitly_wait(1)
    # choose "open in new window"
    achains.context_click(backpack).send_keys(Keys.ARROW_DOWN).send_keys(
        Keys.RETURN
    ).perform()
    assert d.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"
