# TC_001.00.06| Login Page > User is unable to login with wrong username and correct password

from selenium.webdriver.common.keys import Keys

from ..pages.login_page import *


def test_login_wrong_username(d):
    # positive
    page = LoginPage(d, LINK_MAIN)
    page.signin_standart_user(login=USER_NAME_INVALID, password=PASSWORD)
    assert d.current_url == LINK_MAIN

    # negative
    page = LoginPage(d, LINK_MAIN)
    page.open_page()
    page.signin_standart_user(login=USER_NAME_STANDARD, password=PASSWORD)
    assert d.current_url == LINK_INVENTORY
