
from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.CONTENT), "there is no element on page or cant find basket items"

    def should_be_basket_link(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_LINK), 'there is no login link'
