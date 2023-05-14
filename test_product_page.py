import time
import pytest
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


LINK_LOGIN = "http://selenium1py.pythonanywhere.com/accounts/login/"
LINK_CODERS_AT_WORK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
LINK_CITY_AND_STARS = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                 marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])
def test_guest_should_see_login_link_on_product_page_with_parametrize(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


# продублировал функцию(по-умолчанию test_guest_should_see_login_link_on_product_page) для рецензии и сделал 2: 1(
# которая выше) -с параметризацией, 2(оторая ниже) - без параметризации
def test_guest_should_see_login_link_on_product_page_without_parametrize(browser):
    page = ProductPage(browser, LINK_CITY_AND_STARS)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, LINK_CITY_AND_STARS)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, LINK_CODERS_AT_WORK)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket_message()
    basket_page.should_not_be_items_in_basket()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, LINK_CODERS_AT_WORK)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_product_to_basket()
    page.should_be_product_name_in_success_message()
    page.should_be_product_price_in_basket_total()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, LINK_LOGIN)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "testpassword"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, LINK_CODERS_AT_WORK)
        page.open()
        page.should_be_add_to_basket_button()
        page.add_product_to_basket()
        page.should_be_product_name_in_success_message()
        page.should_be_product_price_in_basket_total()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, LINK_CODERS_AT_WORK)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK_CODERS_AT_WORK)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK_CODERS_AT_WORK)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()
