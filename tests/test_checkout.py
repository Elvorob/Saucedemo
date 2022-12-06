import pytest
from selenium.webdriver.common.by import By
from ..pages.login_page import *
from ..pages.inventory_page import *
from ..pages.cart_page import *
from ..pages.locators import *
from ..pages.checkout_page import *

link_inv = "https://www.saucedemo.com/inventory.html"
link_Cart = "https://www.saucedemo.com/cart.html"
link_checkout = "https://www.saucedemo.com/checkout-step-one.html"


# def test_checkout_info_active(d, correct_login):
#     page = InventoryPage(d, link)
#
#     first_item = d.find_element(*InventoryPageLocators.BACKPACK_LABEL)
#     second_item = d.find_element(*InventoryPageLocators.FLEECE_JACKET_LABEL)
#     third_item = d.find_element(*InventoryPageLocators.ONESIE_LABEL)
#     item = InventoryPageLocators()
#     page.add_item_to_cart(
#         item.BACKPACK_ADD_BTN, item.FLEECE_JACKET_ADD_BTN, item.ONESIE_ADD_BTN
#     )
#     page = CartPage(d, link)
#     page.click_icon_cart()
#     assert first_item
#     assert second_item
#     assert third_item
#     d.find_element(*CartPageLocators.BT_CHECKOUT).click()
#     assert (
#         d.find_element(By.XPATH, '//*[text()="Checkout: Your Information"]')
#         and d.current_url == "https://www.saucedemo.com/checkout-step-one.html"
#     )
#     d.find_element(*CheckoutPageLocators.FIRS_NAME).send_keys("Alice")
#     d.find_element(*CheckoutPageLocators.LAST_NAME).send_keys("Smith")
#     d.find_element(*CheckoutPageLocators.ZIP_P_CODE).send_keys(85001)
#
#     d.find_element(*CheckoutPageLocators.CONTINUE).click()
#     assert (
#         d.find_element(By.XPATH, '//*[text()="Checkout: Overview"]')
#         and d.current_url == "https://www.saucedemo.com/checkout-step-two.html"
#     )
#


def test_checkout(d, login_from_list):
    page = InventoryPage(d, link_inv)
    page.add_items_to_cart_for_few_users()

    page = CartPage(d, link_Cart)
    # d.implicitly_wait(2)
    page.go_to_the_cart()
    # assert (
    #     len(d.find_elements(By.CLASS_NAME, "cart_item")) == 3
    # ), "---WRONG NUMBER OF ELEMENTS---"
    assert (
        "Sauce Labs Backpack"
        and "Sauce Labs Bike Light"
        and "Sauce Labs Onesie" in d.find_element(By.CLASS_NAME, "cart_list").text
    )
    d.find_element(*CartPageLocators.BT_CHECKOUT).click()
    assert "checkout-step-one" in d.current_url, "---WRONG URL---"

    page = CheckoutPage(d, link_checkout)
    page.enter_checkout_info("Alice", "Smith", 78717)
    assert "checkout-step-two" in d.current_url, "---WRONG URL---"


def test_checkout_with_data_inspection(d, login_from_list):
    page = InventoryPage(d, link_inv)
    page.add_items_to_cart_for_few_users()

    """создаем словарь ['name':'price'] из товаров, которые добавляем в корзину"""

    items = d.find_elements(
        By.XPATH,
        "//*[@class='btn btn_secondary btn_small btn_inventory']/../../div[@class='inventory_item_label']/a",
    )
    keys_inventory = []
    for k in items:
        keys_inventory.append(k.text)
    prices = d.find_elements(
        By.XPATH, "//*[@class='btn btn_secondary btn_small btn_inventory']/../div"
    )
    values_inventory = []
    for v in prices:
        values_inventory.append(v.text)
    dict_inventory = {
        keys_inventory[i]: values_inventory[i] for i in range(len(keys_inventory))
    }

    """go to cart page, then to chechout page"""

    d.find_element(*InventoryPageLocators.CART_BTN).click()
    assert (
        "Sauce Labs Backpack"
        and "Sauce Labs Bike Light"
        and "Sauce Labs Onesie" in d.find_element(By.CLASS_NAME, "cart_list").text
    )
    d.find_element(*CartPageLocators.BT_CHECKOUT).click()
    assert "checkout-step-one" in d.current_url, "---WRONG URL---"
    page = CheckoutPage(d, link_checkout)
    page.enter_checkout_info("Alice", "Smith", 78717)
    assert "checkout-step-two" in d.current_url, "---WRONG URL---"

    """создаем словарь из товаров, которые указаны на странице checkout:overview"""

    items_ov = d.find_elements(
        By.XPATH,
        "//div[@class='cart_item_label']/a",
    )
    keys_overview = []
    for k in items_ov:
        keys_overview.append(k.text)
    prices_ov = d.find_elements(
        By.XPATH, "//div[@class='cart_item_label']//div[@class='inventory_item_price']"
    )
    values_overview = []
    for v in prices_ov:
        values_overview.append(v.text)
    dict_overview = {
        keys_overview[i]: values_overview[i] for i in range(len(keys_overview))
    }
    assert dict_inventory == dict_overview, "---LISTS ARE NOT THE SAME---"

    """Проверем наличие: Payment, Shipping and Price information (Item total, Tax, Total)"""

    assert (
        d.find_element(
            By.XPATH, "//div[@class='summary_info']/div[@class='summary_info_label'][1]"
        ).text
        == "Payment Information:"
    )
    assert (
        d.find_element(
            By.XPATH, "//div[@class='summary_info']/div[@class='summary_info_label'][2]"
        ).text
        == "Shipping Information:"
    )

    """сравниваем сумму цены товаров с графой Item total"""

    item_total = d.find_element(By.CLASS_NAME, "summary_subtotal_label").text
    item_total_ = float(item_total.replace("Item total: $", ""))

    ammount_ = list(" ".join(values_overview).replace("$", "").split(" "))
    ammount = 0
    for x in ammount_:
        ammount += float(x)

    assert item_total_ == ammount
    d.find_element(*CheckoutPageLocators.FINISH).click()
    assert (
        d.find_element(By.CLASS_NAME, "complete-header").text
        == "THANK YOU FOR YOUR ORDER"
    )
    d.find_element(By.ID, "back-to-products").click()
    assert (
        d.current_url == "https://www.saucedemo.com/inventory.html"
    ), "Page Not Found!!!"


@pytest.mark.parametrize(
    "firstname, lastname, zip",
    [
        ("Alice", "Smith", ""),
        ("Alice", "", "P456"),
        ("", "Smith", "P456"),
        ("", "", ""),
        pytest.param("123", "Smith", "P456", marks=pytest.mark.xfail),
    ],
)
def test_negativ_checkout_data(d, login_from_list, firstname, lastname, zip):
    page = InventoryPage(d, link_inv)
    page.add_items_to_cart_for_few_users()

    page = CartPage(d, link_Cart)
    d.implicitly_wait(2)
    page.go_to_the_cart()
    assert (
        len(d.find_elements(By.CLASS_NAME, "cart_item")) == 3
    ), "---wrong number of elements---"
    # assert ("Sauce Labs Backpack" and "Sauce Labs Bike Light" and "Sauce Labs Onesie"
    #         in d.find_element(By.CLASS_NAME, "cart_list").text
    # )
    d.find_element(*CartPageLocators.BT_CHECKOUT).click()
    assert "checkout-step-one" in d.current_url

    page = CheckoutPage(d, link_checkout)
    page.enter_checkout_info(firstname, lastname, zip)
    assert d.find_element(By.CLASS_NAME, "error-button"), "---MUST BE ERROR BUTTON---"
