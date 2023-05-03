from selenium_utils import webdriver, By, time
import math

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим значение переменной x и рассчитываем значение функции
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = str(math.log(abs(12 * math.sin(int(x)))))

    # Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(y)

    # Отмечаем checkbox и radiobutton
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()

    robots_rule_radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robots_rule_radiobutton.click()

    # Нажимаем на кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()