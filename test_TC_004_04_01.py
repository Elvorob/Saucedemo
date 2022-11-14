import pytest
import time

from pages.cart_page import *


@pytest.mark.xfail(rises="NotWorking")
def test_change_qty(driver, correct_login):
    assert driver.title == "Swag Labs", "____YOU NOT ENTER______"
    driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
    time.sleep(3)
    cart = CartPage(driver, link)
    cart.click_icon_cart()
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]").click()

    time.sleep(3)
