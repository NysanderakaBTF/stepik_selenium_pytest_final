from pages.base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    
    def should_be_add_product_button(self):
        return self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON)
    
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_button.click()

    def get_added_product_name_in_notification(self):
        return self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME_IN_ALERT).text
    
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
    
    def get_cart_total(self):
        return self.browser.find_element(*ProductPageLocators.CART_TOTAL).text
    
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    
    def should_not_be_success_message(self):
        return self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)