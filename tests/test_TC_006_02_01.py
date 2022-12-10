from ..pages.locators import InventoryPageLocators
from ..pages.locators import Widgets

def test_products_page_social_logo(d, correct_login):
    d.find_element(*InventoryPageLocators.APPER_LOGO).click()
    assert d.title == "Swag Labs", "NOT FOUNDED"
    #have social widget
    d.find_element(*Widgets.FB_WIDGET_ALL_PAGES).is_displayed(), "NOT FOUND"
    d.find_element(*Widgets.TWITTER_WIDGET_ALL_PAGES).is_displayed(), "NOT FOUND"
    d.find_element(*Widgets.LINKEDIN_WIDGET_ALL_PAGES).is_displayed(), "NOT FOUND"
