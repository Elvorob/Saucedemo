from ..pages.login_page import LoginPage
from ..pages.inventory_page import InventoryPage
from ..pages.locators import link


def test_remove_item_from_the_cart(d):
    page = LoginPage(d, link)
    page.open_page()
    d.implicitly_wait(30)
    page.signin_4_username("standard_user", "secret_sauce")
    page.should_go_on_product_page()
    page = InventoryPage(d, link)
    page.no_item_in_cart()
    page.add_to_cart_backpack()
    d.implicitly_wait(30)
    page.item_added_to_cart()
    page.remove_backpack_from_cart()
    page.no_item_in_cart()
