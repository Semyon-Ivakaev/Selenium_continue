import time
from .pages.product_page import PageObject
from .pages.base_page import BasePage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = PageObject(browser, link)
    page.open()
    page.click_button_add()
    time.sleep(1)
    page.should_be_alert()
    page.solve_quiz_and_get_code()
    time.sleep(3)
