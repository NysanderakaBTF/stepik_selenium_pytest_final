import time

import pytest
from pages.locators import ProductPageLocators, BasketPageLocators
from pages.product_page import ProductPage
from test_main_page import LoginPage
from pages.basket_page import BasketPage

def test_user_should_see_add_to_cart_button(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    assert page.should_be_add_product_button(), "No add to cart button"
    

    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
    
    
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.open()
    login_page.should_be_login_page()
    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    assert len(basket_page.get_list_of_items()) == 0, "Basket is not empty"
    assert basket_page.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
    

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.email = str(time.time()) + "@fakemail.org"
        self.password = str(time.time())
        page = LoginPage(browser, 'https://selenium1py.pythonanywhere.com/ru/accounts/login/')
        page.open()
        page.register_new_user(self.email, self.password)
        page.should_be_authorized_user()
        
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        product_name_notif = page.get_added_product_name_in_notification()
        product_name = page.get_product_name()
        assert product_name_notif == product_name, "Product name in notification is incorrect"
        
        product_price = page.get_product_price()
        price_in_cart = page.get_cart_total()
        
        assert product_price == price_in_cart, "Product price in cart is incorrect"
        
        assert page.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "No success message after adding to cart"
    
    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)