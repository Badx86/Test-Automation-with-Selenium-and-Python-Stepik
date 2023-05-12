import math
import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


email = ""
password = ""


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(20)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('links', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])
class TestExample:
    def test_example(self, browser, links):
        link = links
        browser.get(link)
        browser.implicitly_wait(20)
        enter_btn = browser.find_element(By.CSS_SELECTOR, "header>nav>div:nth-of-type(4)+a")
        enter_btn.click()
        email_input = browser.find_element(By.ID, "id_login_email")
        email_input.send_keys(email)
        password_input = browser.find_element(By.ID, "id_login_password")
        password_input.send_keys(password)
        login_btn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_btn.click()
        try:
            browser.implicitly_wait(10)
            try_again_btn = browser.find_element(By.CSS_SELECTOR, "button.again-btn")
            try_again_btn.click()
        except NoSuchElementException:
            print("'Solve Again' button is missing")
        finally:
            time.sleep(5)
            input_field = browser.find_element(By.TAG_NAME, "textarea")
            answer = math.log(int(time.time()))
            input_field.send_keys(str(answer))
            send_btn = browser.find_element(By.XPATH, "//button[@class='submit-submission']")
            send_btn.click()
        message_element = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
        message_text = message_element.text
        self.message = message_text
        print(self.message)


if __name__ == "__main__":
    pytest.main()
