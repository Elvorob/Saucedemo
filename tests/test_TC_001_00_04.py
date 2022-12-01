# TC_001.00.04 | Login Page > Verify login with valid password (performance_glitch_user)

# Environment and Test Data:
# Please, choose: Web Version
#
# Test Data
# Username: performance_glitch_user
# Password: secret_sauce
#
# PRECONDITIONS:
# Log in to https://www.saucedemo.com/
#
# STEPS:
#
# Enter Username.
# Enter Password
# Click [Login]
# Expected result:
# The Products page will open.

from ..pages.login_page import *


def test_login_valid_password(d):
    # positive
    page = LoginPage(d, LINK_MAIN)
    page.should_be_login_form()
    page.signin_standart_user(login=USER_NAME_PERFORMANCE_GLITCH, password=PASSWORD)
    assert d.current_url == LINK_INVENTORY

    # negative
    page = LoginPage(d, LINK_MAIN)
    page.open_page()
    page.signin_standart_user(login=USER_NAME_INVALID, password=PASSWORD)
    assert d.current_url == LINK_MAIN
