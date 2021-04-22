from .locators import MainPageLocators
from .locators import BasketPageLocators
from .base_page import BasePage

#pytest -rA -v -m "new"


# class MainPage(BasePage):

# def go_to_login_page(self):
#    login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
#   login_link.click()
#  alert = self.browser.switch_to.alert
# alert.accept()

# def should_be_login_link(self):
#   assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "login is not available"
class MainPage(BasePage):
    def go_to_basket_page(self):
        basket_button = self.browser.find_element(*MainPageLocators.BASKET_LINK)
        basket_button.click()

    def basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.CONTENT), "there is no element on page or cant find basket items"

    def should_be_basket_link(self):
        assert self.is_element_present(*MainPageLocators.BASKET_LINK), 'there is no login link'
