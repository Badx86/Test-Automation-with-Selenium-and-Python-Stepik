import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver


def pytest_make_parametrize_id(config, val): return repr(val)


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     browser.implicitly_wait(30)
#     yield browser
#     print("\nquit browser..")
#     browser.quit()


# @pytest.mark.parametrize('language', ["ru", "en-gb"])
# def test_guest_should_see_login_link(browser, language):
#     link = f"http://selenium1py.pythonanywhere.com/{language}/"
#     browser.get(link)
#     browser.find_element(By.CSS_SELECTOR, "#login_link")
