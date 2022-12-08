import pytest
from ..pages.cart_page import *


@pytest.mark.xfail(rises="NotWorking_BUG,not implemented")
def test_change_qty_plus(d, correct_login):
    d.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
    cart = CartPage(d, link)
    cart.click_icon_cart()
    d.find_element(
        By.XPATH,
        "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]",
    ).click()


@pytest.mark.xfail(rises="NotWorking_BUG,not implemented")
def test_change_dty_minus(d, correct_login):
    d.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
    cart = CartPage(d, link)
    cart.click_icon_cart()
    d.find_element(
        By.XPATH,
        "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]",
    ).click()
