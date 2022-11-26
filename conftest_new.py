import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from .pages.locators import *

"""
-----------------------------------------------------
----------------- DRIVER SELECTION ------------------
-----------------------------------------------------
"""
driver = None
headless = True


def init_driver_chrome():
    o = webdriver.ChromeOptions()
    # o.add_argument("--window-size=1600,1080")
    o.headless = headless
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=o
    )
    return driver


def init_driver_firefox():
    o = webdriver.FirefoxOptions()
    # o.add_argument("--width=1600")
    # o.add_argument("--height=1600")
    o.headless = headless
    driver = webdriver.Chrome(
        service=FirefoxService(GeckoDriverManager().install()), options=o
    )
    return driver


@pytest.fixture(params=["chrome", "firefox"], scope="function", autouse=True)
def d(request):
    global driver
    if driver is not None:
        return driver
    if request.param == "chrome":
        driver = init_driver_chrome()
    elif request.param == "firefox":
        driver = init_driver_firefox()
    else:
        print("Please pass the correct browser name: {}".format(request.param))
        raise Exception("driver is not found")

    return driver


"""
-----------------------------------------------------
--------------- Open and quit browser ---------------
-----------------------------------------------------
"""


@pytest.fixture(scope="function", autouse=True)
def print_browser(d):
    print("\n---------Test started----------\n")
    d.get("https://www.saucedemo.com/")
    yield d
    # d.quit()
    print("\n---------Test ended-----------\n")


"""
-----------------------------------------------------
---------------- HTML-Report Title ------------------
-----------------------------------------------------
"""

# def pytest_html_report_title(report):
#     report.title = "Saucedemo - Let's do it!"

"""
-----------------------------------------------------
---------- Add screenshots to report html -----------
-----------------------------------------------------
"""

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         extra.append(pytest_html.extras.url(driver.current_url))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
#             screenshot = driver.get_screenshot_as_base64()
#             extra.append(pytest_html.extras.image(screenshot, ''))
#         report.extra = extra

"""
-----------------------------------------------------
------------ Sign in with valid username ------------
-----------------------------------------------------
"""


@pytest.fixture(
    params=["standard_user", "problem_user", "performance_glitch_user"],
    scope="function",
)
def login_from_list(d, request):
    d.get("https://www.saucedemo.com/")
    d.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys(request.param)
    d.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("secret_sauce")
    d.find_element(*LoginPageLocators.LOGIN_BTN).click()


@pytest.fixture(scope="function")
def correct_login(d):
    d.get("https://www.saucedemo.com/")
    d.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys(
        LoginPageLocators.USER_NAME
    )
    d.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(
        LoginPageLocators.PASSWORD
    )
    d.find_element(*LoginPageLocators.LOGIN_BTN).click()
    assert (
        d.current_url == "https://www.saucedemo.com/inventory.html"
    ), "____YOU NOT ENTER______"
