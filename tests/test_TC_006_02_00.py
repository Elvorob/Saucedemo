from ..pages.locators import Copywriter, InventoryPageLocators


def test_maine_page_presence_copywriter_robot(d, correct_login):
    d.find_element(*InventoryPageLocators.APPER_LOGO).click()
    assert d.title == "Swag Labs", "NOT FOUNDED"
    copy_text = d.find_element(*Copywriter.FOOTER_COPY).text
    mms = Copywriter()
    assert copy_text in mms.MSG, "copywriter NOT FOUND "
    d.find_element(*Copywriter.IMG_ROBOT).is_displayed(), "IMG Present"
