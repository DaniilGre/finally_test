from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_link()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_all_field_required_to_registration(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_FOR_REGISTRATION), 'there is no EMAIL_FOR_REGISTRATION'
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FIRST_REGISTRATION), 'there is no PASSWORD'
        assert self.is_element_present(*LoginPageLocators.PASSWORD_CHECK_RIGHT_REGISTRATION), 'there is no PASSWORD_CHECK_RIGHT_REGISTRATION'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT), 'there is no REGISTRATION_SUBMIT'

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FOR_REGISTRATION)
        email_field.send_keys(email)

        password_field_first = self.browser.find_element(*LoginPageLocators.PASSWORD_FIRST_REGISTRATION)
        password_field_first.location_once_scrolled_into_view
        password_field_first.send_keys(password)

        password_field_second = self.browser.find_element(*LoginPageLocators.PASSWORD_CHECK_RIGHT_REGISTRATION)
        password_field_second.location_once_scrolled_into_view
        password_field_second.send_keys(password)

        registration_button_submit = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        registration_button_submit.location_once_scrolled_into_view
        registration_button_submit.click()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There is no login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "There is no login form"
