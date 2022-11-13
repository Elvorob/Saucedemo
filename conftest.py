import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from .pages.locators import *

@pytest.fixture(scope='function')
def driver():
    o = webdriver.ChromeOptions()
    o.headless = False
    print('\nstart browser...')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=o)
    yield driver
    print('\nquit browser...')
    driver.quit()

@pytest.fixture(scope="function")
def correct_login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys(LoginPageLocators.USER_NAME)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(LoginPageLocators.PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_BTN).click()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "____YOU NOT ENTER______"

