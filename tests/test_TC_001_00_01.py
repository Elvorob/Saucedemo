import pytest
from pages.login_page import *

# from .pages.cart_page import *

link_Main = "https://www.saucedemo.com/"


def test_standart_user_can_signin(d):
    assert d.title == "Swag Labs"
    page = LoginPage(d, link_Main)
    page.should_be_login_form()
    page.signin_standart_user(login="standard_user", password="secret_sauce")
    page.should_go_on_product_page()


@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
        pytest.param("locked_out_user", "secret_sauce", marks=pytest.mark.xfail),
    ],
)
def test_signin_4_username(d, username, password):
    page = LoginPage(d, link_Main)
    page.should_be_login_form()
    page.signin_4_username(username, password)
    page.should_go_on_product_page()
