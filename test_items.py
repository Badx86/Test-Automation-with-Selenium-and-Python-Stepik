import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)  # необходимо по условию задачи(для рецензирования)
    wait = WebDriverWait(browser, 10)
    add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket")))
    assert add_to_cart_button is not None, "Add to cart button is not found"
