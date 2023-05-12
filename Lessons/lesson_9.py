from selenium_utils import webdriver, By, time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    # Найти все элементы селектора и вычислить их сумму
    num1 = int(browser.find_element(By.CSS_SELECTOR, "#num1").text)
    num2 = int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
    answer = num1 + num2

    # Выбрать ответ из выпадающего списка и отправить форму
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(answer))
    submit_btn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()


finally:
    time.sleep(10)
    browser.quit()