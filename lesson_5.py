from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element(By.CSS_SELECTOR, "input[name='first_name']")
    first_name.send_keys("qwe")
    last_name = browser.find_element(By.CSS_SELECTOR, "input[name='last_name']")
    last_name.send_keys("rty")
    city_name = browser.find_element(By.CSS_SELECTOR, "input[class='form-control city']")
    city_name.send_keys("asd")
    email = browser.find_element(By.CSS_SELECTOR, "#country")
    email.send_keys("qwerty@mail.com")
    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button[normalize-space()='Submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    time.sleep(30)
    browser.quit()