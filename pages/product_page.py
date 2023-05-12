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


