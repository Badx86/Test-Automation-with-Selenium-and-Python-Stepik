from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest
import os
import time


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru, en-gb, es, fr")


@pytest.fixture(scope="function")
def browser(request):
    # В переменную user_language передается параметр из командной строки
    user_language = request.config.getoption("language")
    # Инициализируются опции браузера
    options = Options()
    # В опции вебдрайвера передаем параметр из командной строки
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    # Делаем скриншот, если тест падает
    if call.when == 'call' and call.excinfo is not None:
        timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
        test_name = item.nodeid.replace("::", "_") + "_" + timestamp
        browser = item.funcargs['browser']
        browser.save_screenshot(f'screenshots/{test_name}.png')