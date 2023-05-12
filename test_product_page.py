from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    product_name = page.get_product_name()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_msg()
    assert product_name == page.get_success_message_product_name(), "Product name does not match"
    page.should_be_basket_total()

