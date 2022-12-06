import pytest
from ..pages.login_page import *
from ..pages.locators import *

link_Main = "https://www.saucedemo.com/"


@pytest.mark.parametrize(
    "username,password",
    [
        ("", ""),
        ("standartUser", "secret_sauce"),
        ("standard_user", "secretsauce"),
        ("standard_user", ""),
        ("", "secret_sauce"),
        ("locked_out_user", "secret_sauce"),
    ],
)
def test_negativ_signin(d, username, password):
    page = LoginPage(d, link_Main)
    page.should_be_login_form()
    page.signin_4_username(username, password)
    assert d.find_element(By.XPATH, "//*[contains(text(), 'Epic sadface')]")


def test_signin_using_a_list_of_credentials(d, login_from_list):
    assert d.title == "Swag Labs"
    assert "inventory" in d.current_url


@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
    ],
)
def test_logout(d, username, password):
    page = LoginPage(d, link_Main)
    page.should_be_login_form()
    page.signin_4_username(username, password)
    page.should_go_on_product_page()

    d.find_element(*InventoryPageLocators.BURGER_BTN).click()
    d.find_element(*InventoryPageLocators.BURGER_MENU_LOGOUT_BTN).click()
    assert d.current_url == link_Main
