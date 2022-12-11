from ..pages.locators import link
from ..pages.login_page import LoginPage


def test_login_page_with_empty_password(d):
    page = LoginPage(d, link)
    page.open_page()
    page.signin_4_username("standard_user", "")
    page.user_is_not_authorized()
