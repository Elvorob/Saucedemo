import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from .pages.locators import *
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.core.utils import ChromeType

@pytest.fixture(scope='function')
def driver():
    o = webdriver.ChromeOptions()
    o.headless = False
    print('\nstart browser...')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=o)
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

@pytest.fixture(scope="class")
def d(browser):
    if browser == "firefox":
        o = webdriver.FirefoxOptions()
        o.headless = True
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()), options=o
        )
    else:
        o = webdriver.ChromeOptions()
        o.headless = False
        driver = webdriver.Chrome(
            service=ChromeService(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
            ),
            options=o,
        )
    return driver


# ------- 2 функции определяют параметр, котрый принимает pytest (browser)
def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", help="define browser: chrome or firefox, --firefox"
    )
# ------- browser сами назвали так параметр
# ------- default - что будет запускаться по умолчанию
@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")

######################################################################
@pytest.fixture(scope="class", autouse=True)
def g(d):
    print("\n***** start fixture = setup *****\n")
    d.get("https://www.saucedemo.com/")
    yield d
    d.quit()
    print("\n***** end fixture = teardown *****\n")