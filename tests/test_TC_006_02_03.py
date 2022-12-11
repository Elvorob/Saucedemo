from ..pages.locators import InventoryPageLocators, Copywriter


def test_cart_page_copywriter(d, correct_login):
    d.find_element(*InventoryPageLocators.CART_BTN).click()
    d.find_element(*InventoryPageLocators.APPER_LOGO).click()
    assert d.title == "Swag Labs", "NOT FOUNDED"
    a = d.find_element(*Copywriter.FOOTER_COPY)
    mms = Copywriter()
    assert a.text == mms.MSG, "copywriter NOT FOUND"
    assert d.find_element(*Copywriter.IMG_ROBOT).is_displayed(), "ING NOT FOUND"
