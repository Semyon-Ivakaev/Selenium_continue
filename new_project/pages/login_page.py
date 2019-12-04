from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "Login link is not found"
        # красный тест assert "login" in self.browser.current_url, "'login' not in curren url"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.login_link), "Login form not found"
        
    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.registr_link), "Registr form not found"