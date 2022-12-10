from ..pages.cart_page import CartPage
from ..pages.locators import CheckoutPageLocators, InventoryPageLocators, CartPageLocators, link
from ..pages.checkout_page import CheckoutPage


def test_finish_shopping(d, correct_login):
    d.find_element(*InventoryPageLocators.RED_TSHIRT_ADD_BTN).click()
    cart = CartPage(d, link)
    cart.click_icon_cart()
    d.find_element(*CartPageLocators.BT_CHECKOUT).click()
    page_ch_you_inf = d.find_element(*CheckoutPageLocators.TITLE_YOU_INFO)
    assert page_ch_you_inf.text == "CHECKOUT: YOUR INFORMATION", "Page not found!!!"
    pages_e = CheckoutPage(d, correct_login)
    pages_e.enter_checkout_info("Test", "Test", 1234)
    loc = CheckoutPageLocators()
    assert (
            d.current_url == loc.OVERVIEW_LINK
    ), "Not Found"
    d.find_element(*CheckoutPageLocators.FINISH).click()
    complete_msg_text = d.find_element(*CheckoutPageLocators.HEADER_THX).text
    assert complete_msg_text == loc.MSS_THXY
    print("______THANKS FOR YOUR ORDER_____")
    pages_e.back_home()
