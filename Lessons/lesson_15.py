from selenium.webdriver.common.by import By
from selenium_utils import webdriver


link_01 = "http://suninjuly.github.io/registration1.html"
link_02 = "http://suninjuly.github.io/registration2.html"


def test_registration_01():
    browser = webdriver.Chrome()
    browser.get(link_01)
    first_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    first_name.send_keys("qwe")
    last_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    last_name.send_keys("asd")
    email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    email.send_keys("zxc@mail.com")
    submit_button = browser.find_element(By.XPATH, "//button[normalize-space()='Submit']")
    submit_button.click()
    successful_reg = "//h1[normalize-space()='Congratulations! You have successfully registered!']"
    actual_text = browser.find_element(By.XPATH, successful_reg).text
    expected_text = "Congratulations! You have successfully registered!"
    assert actual_text == expected_text

    browser.quit()


def test_registration_02():
    browser = webdriver.Chrome()
    browser.get(link_02)
    first_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    first_name.send_keys("qwe")
    email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    email.send_keys("zxc@mail.com")
    submit_button = browser.find_element(By.XPATH, "//button[normalize-space()='Submit']")
    submit_button.click()
    expected_text = "Congratulations! You have successfully registered!"
    actual_text = "Congratulations! You have successfully registered!"
    assert actual_text == expected_text

    browser.quit()


