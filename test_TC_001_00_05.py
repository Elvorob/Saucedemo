from .pages.locators import LoginPageLocators, link
import time


"""TC_001.00.05| Login Page >
User is unable to login with empty username and password"""


def test_login_page_with_empty_fields(d):
    d.get("https://www.saucedemo.com/")
    d.find_element(*LoginPageLocators.USERNAME_INPUT).clear()
    d.find_element(*LoginPageLocators.PASSWORD_INPUT).clear()

    d.find_element(*LoginPageLocators.LOGIN_BTN).click()
    time.sleep(2)

    assert (
        d.find_element(*LoginPageLocators.MESSAGE_EPIC_SADFACE).text
        == "Epic sadface: Username is required"
        and d.current_url == link
    )


def test_login_page_with_empty_fields_2(d):
    d.get("https://www.saucedemo.com/")
    user_name = d.find_element(*LoginPageLocators.USERNAME_INPUT)
    password = d.find_element(*LoginPageLocators.PASSWORD_INPUT)
    assert user_name.get_attribute("value") == ""
    assert password.get_attribute("value") == ""

    d.find_element(*LoginPageLocators.LOGIN_BTN).click()
    time.sleep(2)

    assert (
        d.find_element(*LoginPageLocators.MESSAGE_EPIC_SADFACE).text
        == "Epic sadface: Username is required"
        and d.current_url == link
    )
