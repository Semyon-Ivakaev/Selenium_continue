import time
import pytest
from .pages.product_page import PageObject
from .pages.base_page import BasePage

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):   
    page = PageObject(browser, link)
    page.open()
    page.click_button_add()
    time.sleep(1)
    page.is_not_element_present()#это не работает, локаторы похоже нужны

'''
@pytest.mark.parametrize('link', [
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail), #пометили багнутую ссылку, которая падает
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = link
    page = PageObject(browser, link)
    page.open()
    page.click_button_add()
    time.sleep(1)
    page.should_be_alert()
    page.solve_quiz_and_get_code()
    page.should_be_book_name()
    time.sleep(3)
'''


