from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    EMAIL_FOR_REGISTRATION = (By.CSS_SELECTOR, '[name="registration-email"]')
    PASSWORD_FIRST_REGISTRATION = (By.CSS_SELECTOR,'[name="registration-password1"]')
    PASSWORD_CHECK_RIGHT_REGISTRATION = (By.CSS_SELECTOR,'[name="registration-password2"]')
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, '[name="registration_submit"]')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class ProductPageLocators:
    BUTTON_ADD_TO_CARD = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_BEFORE_ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, ".col-sm-6.product_main p.price_color")
    NAME_OF_PRODUCT_EXPECTED = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    NAME_OF_ACTUAL_PRODUCT = (By.CSS_SELECTOR, ".alertinner strong")
    MESSAGE_WITH_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasketPageLocators:
    CONTENT = (By.CSS_SELECTOR,"#content_inner > p")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-default[href]")

