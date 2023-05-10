import math
import time
import pytest
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import ChromiumDriver

link = "https://stepik.org/lesson/236895/step/1"
email = "qwerty@gmail.com"
password = "qwerty"


class TestExample:
    message = ""
    links = [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"
    ]

    @pytest.fixture(scope="function")
    def browser(self):
        print("\nstart browser for test..")
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.implicitly_wait(30)
        yield browser
        print("\nquit browser..")
        browser.quit()

    @pytest.mark.parametrize('links', links)
    def test_example(self, browser, links):
        browser.get(links)
        browser.implicitly_wait(10)
        sign_in_btn = browser.find_element(By.CSS_SELECTOR, "header>nav>div:nth-of-type(4)+a")
        sign_in_btn.click()
        login_field = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.ID, "id_login_email")))
        login_field.send_keys(email)
        password_field = browser.find_element(By.ID, "id_login_password")
        password_field.send_keys(password)
        submit_btn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_btn.click()
        try:
            input_field = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/article[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/textarea[1]")))
            browser.implicitly_wait(10)
            input_field.send_keys(str(math.log(float(time.time()))))
        except StaleElementReferenceException:
            pass
        send_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='submit-submission']"))
        )
        send_btn.click()
        message_element = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
        )
        message_text = message_element.text
        self.message += message_text
        print(self.message)


if __name__ == "__main__":
    pytest.main()
