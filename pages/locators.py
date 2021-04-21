from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BUTTON_ADD_TO_CARD = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_BEFORE_ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, ".col-sm-6.product_main p.price_color")
    NAME_OF_PRODUCT_EXPECTED = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    NAME_OF_ACTUAL_PRODUCT = (By.CSS_SELECTOR, ".alertinner strong")
    MESSAGE_WITH_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
