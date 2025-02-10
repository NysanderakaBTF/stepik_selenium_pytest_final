from pages.base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    
    def success_message_should_have_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
    
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
    
    def should_be_success_message(self):
        return self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
    
    def product_price_should_match_added_price(self):
        added_price = self.get_product_price()
        cart_total = self.get_cart_total()
        assert added_price == cart_total, "Product price in cart is incorrect"
        
    def product_name_should_match_name_in_notification(self):
        product_name_notif = self.get_added_product_name_in_notification()
        product_name = self.get_product_name()
        assert product_name_notif == product_name, "Product name in notification is incorrect"
        