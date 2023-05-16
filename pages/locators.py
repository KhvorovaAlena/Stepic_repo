from selenium.webdriver.common.by import By


#class MainPageLocators():


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    ALERT_WITH_PRODUCT_NAME = (By.XPATH, "//*[@id='messages']/div[1]")
    ALERT_WITH_PRODUCT_PRICE = (By.XPATH, "//*[@id='messages']/div[3]")
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, ".alert-success strong")
    PRODUCT_PRICE_IN_CART = (By.CSS_SELECTOR, ".alert-info p strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group")

class BasketPageLocators():
    ITEMS_SECTION = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
