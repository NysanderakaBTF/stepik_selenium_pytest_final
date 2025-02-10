from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    
    def is_basket_page(self):
        assert "basket" in self.browser.current_url, "Basket page is not opened"
        
    def get_list_of_items(self):
        return self.browser.find_elements(*BasketPageLocators.PRODUCT_ROW)