from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    ################################################################
    def should_be_login_form(self):
        self.should_be_login_box()
        self.should_be_login_btn()

    def should_be_login_box(self):
        assert self.driver.find_elements(*LoginPageLocators.LOGIN_BOX)

    def should_be_login_btn(self):
        assert self.driver.find_element(*LoginPageLocators.LOGIN_BTN)

    ################################################################
    def signin_4_username(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    ################################################################
    def signin_standart_user(self, login="login", password="password"):
        self.driver.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys(login)
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BTN).click()

    def should_go_on_product_page(self):
        assert "inventory" in self.driver.current_url

    def signin_locked_out_user(self, login="login", password="password"):
        self.driver.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys(login)
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BTN).click()
        # self.driver.implicitly_wait(2)
        message = self.driver.find_element(*LoginPageLocators.MESSAGE_EPIC_SADFACE)
        value = message.text
        assert value == "Epic sadface: Sorry, this user has been locked out."

    def signin_empty_login_valid_password(self, password="password"):
        self.driver.find_element(*LoginPageLocators.USERNAME_INPUT).clear()
        password_input = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BTN).click()
        message = self.driver.find_element(*LoginPageLocators.MESSAGE_EPIC_SADFACE)
        value = message.text
        assert value == "Epic sadface: Username is required"

    def login_password(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys(*LoginPageLocators.USER_NAME)
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(*LoginPageLocators.PASSWORD)
        self.driver.find_element(*LoginPageLocators.LOGIN_BTN).click()
