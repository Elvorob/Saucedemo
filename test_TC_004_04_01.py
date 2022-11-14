import pytest
import time

from .pages.cart_page import *


@pytest.mark.xfail(rises="NotWorking")
def test_change_qty(d, correct_login):
    assert d.title == "Swag Labs", "____YOU NOT ENTER______"
    d.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()

    time.sleep(3)

    cart = CartPage(d, link)
    cart.click_icon_cart()
    d.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]").click()

