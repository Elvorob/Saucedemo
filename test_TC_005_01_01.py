import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.xfail(rises="NotReset")
def test_reset_app(driver, correct_login):
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "")
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(2)
    driver.find_element(By.ID, "reset_sidebar_link").click()
    assert driver.find_element(By.ID, "remove-sauce-labs-backpack").text == "ADD TO CART", "NOT RESET"