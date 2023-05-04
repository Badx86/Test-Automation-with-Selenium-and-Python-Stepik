from selenium_utils import webdriver, By, time
import math

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_click = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_click.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    y = math.log(abs(12*math.sin(x)))

    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(y)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()




finally:
    time.sleep(10)
    browser.quit()