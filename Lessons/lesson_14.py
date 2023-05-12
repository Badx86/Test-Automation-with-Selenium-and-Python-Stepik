from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium_utils import webdriver
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book = browser.find_element(By.ID, "book")
    book.click()

    x = int(browser.find_element(By.ID, "input_value").text)
    y = math.log(abs(12*math.sin(x)))
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    answer = alert_text
    print(answer)


finally:

    time.sleep(30)
    browser.quit()