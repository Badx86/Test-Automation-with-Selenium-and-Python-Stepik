from selenium_utils import webdriver, By, time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter first name']")
    first_name.send_keys("qwe")

    last_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter last name']")
    last_name.send_keys("rty")

    email = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter email']")
    email.send_keys("qwerty@mail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "../TEST_SHIT.txt"
    file_path = os.path.join(current_dir, file_name)
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()