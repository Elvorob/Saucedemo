from ..pages.login_page import LoginPage
from ..pages.inventory_page import InventoryPage
from ..pages.locators import link


def test_return_from_itempage(d):
    page = LoginPage(d, link)
    page.open_page()
    d.implicitly_wait(30)
    page.signin_4_username("standard_user", "secret_sauce")
    d.implicitly_wait(30)
    page.should_go_on_product_page()
    page = InventoryPage(d, link)
    page.go_to_backpack_item_page()
    d.implicitly_wait(30)
    page.go_back_from_itempage_to_inventorypage()
