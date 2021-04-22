# pytest -rA -v test_product_page.py
import pytest
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from time import sleep
import time


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        page.should_be_all_field_required_to_registration()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + str(time.time())
        page.register_new_user(email, password)
        browser.implicitly_wait(10)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4"
        page_with_product = ProductPage(browser, link)
        page_with_product.open()
        page_with_product.should_find_add_button()
        page_with_product.add_product_to_basket()
        page_with_product.solve_quiz_and_get_code()
        page_with_product.should_be_message_about_add()
        page_with_product.should_be_message_about_add_with_price()
        page_with_product.actual_name_in_the_basket()
        page_with_product.actual_price_in_the_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    page.basket_is_empty()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4"
    page_with_product = ProductPage(browser, link)
    page_with_product.open()
    page_with_product.should_find_add_button()
    page_with_product.add_product_to_basket()
    page_with_product.solve_quiz_and_get_code()
    page_with_product.should_be_message_about_add()
    page_with_product.should_be_message_about_add_with_price()
    page_with_product.actual_name_in_the_basket()
    page_with_product.actual_price_in_the_basket()
