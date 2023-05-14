from .base_page import BasePage
from .locators import ProductPageLocators, BasketPageLocators
from .basket_page import BasketPage


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
        product_price_element = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price_element.text.strip()

    def get_success_message_product_name(self):
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MSG).text
        product_name = success_message.split(" has been added to your basket.")[0]
        return product_name

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MSG), "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MSG), "Success message should disappear, but it is still present"

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        basket_link.click()
        return BasketPage(self.browser, self.browser.current_url)

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "Add to basket button is not present"

    def should_be_product_name_in_success_message(self):
        product_name_in_msg = self.get_success_message_product_name()
        actual_product_name = self.get_product_name()
        assert product_name_in_msg == actual_product_name, "Product name in success message does not match actual product name"

    def get_basket_total_message_product_price(self):
        basket_total_message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MSG).text
        product_price_in_basket_total = basket_total_message.split()[-1]
        return product_price_in_basket_total

    def should_be_product_price_in_basket_total(self):
        product_price_in_basket_total = self.get_basket_total_message_product_price()
        actual_product_price = self.get_product_price()
        assert product_price_in_basket_total == actual_product_price, "Product price in basket total does not match actual product price"
