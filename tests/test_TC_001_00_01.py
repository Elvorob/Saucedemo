import pytest
from ..pages.login_page import *


@pytest.mark.elina_abramova
def test_standart_user_can_signin(d):
    assert d.title == "Swag Labs"
    page = LoginPage(d, LINK_MAIN)
    page.should_be_login_form()
    page.signin_standart_user(login=USER_NAME_STANDARD, password=PASSWORD)
    page.should_go_on_product_page()
