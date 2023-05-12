from itertools import product
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def should_be_success_msg(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MSG), "Success message is not present"

    def should_be_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MSG), "Basket total message is not present"

    def get_product_name(self):
        product_name_element = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name_element.text

    def get_product_price(self):
        product_price_element = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text.strip()
        return product_price_element

    def get_success_message_product_name(self):
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MSG).text
        expected_message = "Coders at Work has been added to your basket."
        assert success_message == expected_message, "Unexpected success message: {}".format(success_message)
        product_name = success_message.split(" has been added to your basket.")[0]
        return product_name

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MSG), "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MSG), "Success message should disappear, but it is still present"

