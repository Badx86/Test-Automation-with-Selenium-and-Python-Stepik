from selenium_utils import webdriver, By, time
import math

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    y = math.log(abs(12*math.sin(x)))
    # Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(y)

    # Отмечаем checkbox и radiobutton
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()

    robots_rule_radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robots_rule_radiobutton)
    robots_rule_radiobutton.click()

    # Нажимаем на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()


finally:
    time.sleep(3)
    browser.quit()