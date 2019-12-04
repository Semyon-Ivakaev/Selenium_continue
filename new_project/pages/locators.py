from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    login_link = (By.CSS_SELECTOR, "#login_form")
    registr_link = (By.CSS_SELECTOR, "#register_form")
