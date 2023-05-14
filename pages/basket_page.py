from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MSG), \
            "Empty basket message is not present"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items are present, but should not be"

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        basket_link.click()
