from .locators import ButtonAddLocators
from .base_page import BasePage
#from .locators import FindAlert

class PageObject(BasePage):
    def click_button_add(self):
        button_add = self.browser.find_element(*ButtonAddLocators.button).click()

    def should_be_alert(self):
        #alert = self.browser.switch_to.alert
        assert self.browser.switch_to.alert, "Alert window not found"
'''
    def should_be_alert(self):
        assert self.is_elemet_present(*FindAlert.alert), "Alert window not found"
'''
