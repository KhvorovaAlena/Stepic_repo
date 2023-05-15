from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def add_item_in_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def check_product_price_and_name(self):
        self.check_product_price()
        self.check_product_name()

    def check_product_price(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.ALERT_WITH_PRODUCT_PRICE))
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).get_attribute("textContent")
        product_price_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_CART).get_attribute("textContent")
        assert product_price == product_price_in_cart, f"Product price {product_price} does not equal with cart price {product_price_in_cart}"
        print(f"Product price {product_price}, product price in the cart {product_price_in_cart}")

    def check_product_name(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.ALERT_WITH_PRODUCT_NAME))
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).get_attribute("textContent")
        product_name_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_CART).get_attribute("textContent")
        assert product_name == product_name_in_cart, f"Product name {product_name} does not equal with product name in the cart {product_name_in_cart}"
        print(f"Product name {product_name}, product name in the cart {product_name_in_cart}")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_WITH_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_WITH_PRODUCT_NAME), \
            "Success message did not disappear, but should be"



