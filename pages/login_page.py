from pages.locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "'login' is not present in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present on login page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present on login page"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_field.send_keys(email)
        
        pass1_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        pass1_field.send_keys(password)
        
        pass2_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRMATION)
        pass2_field.send_keys(password)
        
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_BUTTON)
        register_button.click()
    