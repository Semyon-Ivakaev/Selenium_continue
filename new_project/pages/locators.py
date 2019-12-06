from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    basket_button = (By.CSS_SELECTOR, "span a.btn.btn-default")
    
class LoginPageLocators():
    login_link = (By.CSS_SELECTOR, "#login_form")
    registr_link = (By.CSS_SELECTOR, "#register_form")

class ButtonAddLocators():
    button = (By.CSS_SELECTOR, "#add_to_basket_form button")

class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items .row")
    ALERT = (By.CSS_SELECTOR, "div#content_inner p")
