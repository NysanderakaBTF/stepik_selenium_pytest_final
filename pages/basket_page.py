from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    
    def is_basket_page(self):
        assert "basket" in self.browser.current_url, "Basket page is not opened"
        
    def get_list_of_items(self):
        return self.browser.find_elements(*BasketPageLocators.PRODUCT_ROW)
    
    def should_be_empty_basket_message(self):
        return self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
    
    def should_be_basket_empty(self):
        assert len(self.get_list_of_items()) == 0, "Basket is not empty"