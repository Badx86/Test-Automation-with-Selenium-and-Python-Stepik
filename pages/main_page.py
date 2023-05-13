from .base_page import BasePage
from .basket_page import BasketPage
from .locators import MainPageLocators, BasketPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        basket_link.click()
        return BasketPage(self.browser, self.browser.current_url)
