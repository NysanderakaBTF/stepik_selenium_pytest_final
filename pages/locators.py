from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    CART_TOTAL = (By.XPATH, "//div[contains(@class, 'alert-info')]//strong")
    PRODUCT_NAME = (By.XPATH, '//div[contains(@class,"product_main")]/h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")
    ADDED_PRODUCT_NAME_IN_ALERT = (By.CSS_SELECTOR, "div.alert div strong")
    ALERT_ADDED_TO_CART = (By.CSS_SELECTOR, "div.alert-info div strong")
    ALERT_WARNING = (By.CSS_SELECTOR, "div.alert-warning")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.XPATH, "//div[contains(@class, 'basket')]/span/a[contains(@class, 'btn')]")

class BasketPageLocators():
    PRODUCT_ROW = (By.CSS_SELECTOR, "div.basket-items")
    PRODUCT_NAME_IN_BASKET = (By.XPATH, "//div[@class='basket-items']//h3/a")
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//div[@id='content_inner']/p")