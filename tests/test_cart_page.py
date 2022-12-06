import pytest
from ..pages.locators import *
from ..pages.inventory_page import *
from ..pages.cart_page import *

link_inv = "https://www.saucedemo.com/inventory.html"
link_Cart = "https://www.saucedemo.com/cart.html"


def test_open_cart(d, login_from_list):
    assert d.title == "Swag Labs", "NOT ENTER"
    d.find_element(*InventoryPageLocators.CART_BTN).click()
    assert d.current_url == "https://www.saucedemo.com/cart.html"
    d.find_element(*CartPageLocators.CONTINUE_SHOPPING).click()
    assert d.title == "Swag Labs", "____You NOT LEFT_____"


def test_add_items(d, login_from_list):
    page = InventoryPage(d, link_inv)
    d.implicitly_wait(2)
    page.add_backpack_for_few_users()


def test_remove_items_from_cart_on_cart_page(d, login_from_list):
    page = InventoryPage(d, link_inv)
    page.add_backpack_for_few_users()
    page = CartPage(d, link_Cart)
    d.implicitly_wait(2)
    page.backpack_can_be_removed()
    page.cart_is_empty()


@pytest.mark.xfail(rises="NotWorking")
def test_change_qty(d, correct_login):
    d.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
    cart = CartPage(d, link)
    cart.click_icon_cart()
    d.find_element(
        By.XPATH,
        "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]",
    ).click()


@pytest.mark.xfail
def test_checkout_with_empty_cart(d, correct_login):
    page = CartPage(d, link_inv)
    page.go_to_the_cart()
    page.cart_is_empty()
    page.chackout_order_with_empty_cart()
