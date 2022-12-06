import time

import pytest
from selenium.webdriver.common.by import By

from ..pages.locators import *
from ..pages.login_page import *
from ..pages.inventory_page import *
from ..pages.checkout_page import *


def test_about_page_all_users(d, login_from_list):
    d.find_element(*InventoryPageLocators.BURGER_BTN).click()
    d.find_element(*InventoryPageLocators.BURGER_MENU_ABOUT_BTN).click()
    assert d.current_url == "https://saucelabs.com/"


@pytest.mark.xfail(rises="NotReset")
def test_reset_app(d, correct_login):
    d.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    d.find_element(By.ID, "")
    d.find_element(By.ID, "react-burger-menu-btn").click()
    d.find_element(By.ID, "reset_sidebar_link").click()
    assert (
        d.find_element(By.ID, "remove-sauce-labs-backpack").text == "ADD TO CART"
    ), "NOT RESET"


def test_widget_FB(d, correct_login):
    d.find_element(By.XPATH, '//a[contains(text(),"Facebook")]').click()
    handles = d.window_handles
    d.switch_to.window(handles[1])
    url = d.current_url
    assert (
        "https://www.facebook.com" in url and "saucelabs" in url
    ), "you are NOT on correct Facebook page"


def test_widgets_inventory_page(d, correct_login):
    link = "https://www.saucedemo.com/inventory.html"
    page = InventoryPage(d, link)
    page.open_page()
    page.all_widgets_on_page()


def test_widgets_inventory_item_page(d, correct_login):
    link = "https://www.saucedemo.com/inventory-item.html?id=4"
    page = InventoryPage(d, link)
    page.open_page()
    page.all_widgets_on_page()


def test_widgets_cart_page(d, correct_login):
    link = "https://www.saucedemo.com/cart.html"
    page = InventoryPage(d, link)
    page.open_page()
    page.all_widgets_on_page()


def test_widgets_checkout_step_one_page(d, correct_login):
    link = "https://www.saucedemo.com/inventory.html"
    page = InventoryPage(d, link)
    page.add_to_cart_backpack()
    link = "https://www.saucedemo.com/checkout-step-one.html"
    page = CheckoutPage(d, link)
    page.open_page()
    page.all_widgets_on_page()


def test_widgets_checkout_step_two_page(d, correct_login):
    link = "https://www.saucedemo.com/inventory.html"
    page = InventoryPage(d, link)
    page.add_to_cart_backpack()
    link = "https://www.saucedemo.com/checkout-step-one.html"
    page = CheckoutPage(d, link)
    page.open_page()
    page.enter_checkout_info("Elena", "Precrasnaya", "11100")
    page.all_widgets_on_page()


def test_widgets_checkout_complete_page(d, correct_login):
    link = "https://www.saucedemo.com/inventory.html"
    page = InventoryPage(d, link)
    page.add_to_cart_backpack()
    link = "https://www.saucedemo.com/checkout-step-one.html"
    page = CheckoutPage(d, link)
    page.open_page()
    page.enter_checkout_info("Elena", "Precrasnaya", "11100")
    page.d.find_element(*CheckoutPageLocators.FINISH).click()
    page.all_widgets_on_page()


def test_mp_presence_copywriter_robot(d, correct_login):
    d.find_element(By.CLASS_NAME, "app_logo").click()
    assert d.title == "Swag Labs", "NOT FOUNDED"
    a = d.find_element(By.CLASS_NAME, "footer_copy")
    assert (
        a.text
        == "© 2022 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"
    ), ("copywriter NOT " "FOUND ")
    img = d.find_element(
        By.XPATH, '//body/div[@id="root"]/div[@id="page_wrapper"]/footer[1]/img[1]'
    )
    print(f"IMG Present_{img.is_displayed()}")


def test_pp_social_logo(d, correct_login):
    d.find_element(By.CLASS_NAME, "app_logo").click()
    assert d.title == "Swag Labs", "NOT FOUNDED"
    d.find_element(By.CLASS_NAME, "social").is_displayed(), "NOT FOUND"


def test_cart_page_copywriter(d, correct_login):
    d.find_element(*InventoryPageLocators.CART_BTN).click()
    d.find_element(By.CLASS_NAME, "app_logo").click()
    assert d.title == "Swag Labs", "NOT FOUNDED"
    a = d.find_element(By.CLASS_NAME, "footer_copy")
    assert (
        a.text
        == "© 2022 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"
    ), "copywriter NOT FOUND"
    img = d.find_element(
        By.XPATH, '//body/div[@id="root"]/div[@id="page_wrapper"]/footer[1]/img[1]'
    )
    if "ng-hide" in img.get_attribute("class"):
        print("Image is not visible on screen")
    else:
        print("Image is visible on screen")
