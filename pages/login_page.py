from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_INPUT)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT)
        password_input.send_keys(password)
        confirm_password_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_INPUT)
        confirm_password_input.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        register_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализация проверки на корректный url адрес
        assert "login" in self.browser.current_url, "Login URL is not correct"

    def should_be_login_form(self):
        # реализация проверки, что форма логина представлена на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), "Submit button is present on the page"

    def should_be_register_form(self):
        # реализация проверки, что форма регистрации представлена на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT), "Submit button is present on the page"

