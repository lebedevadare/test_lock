import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from variables import URL


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default=URL, help="choose your browser")


@pytest.fixture
def browser(request):
    browser_param = request.config.getoption("--browser")
    if browser_param == "chrome":
        options = Options()
        options.page_load_strategy = 'normal'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    else:
        raise Exception(f"{request.param} is not supported!")
    print("браузер открылся")
    driver.implicitly_wait(20)
    request.addfinalizer(driver.close)
    driver.get(request.config.getoption("--url"))

    return driver


class GetURL:
    def __init__(self, base_address):
        self.base_address = base_address

    def get_url(self, path):
        url = f"{self.base_address}{path}"
        return url


@pytest.fixture
def url_path():
    return GetURL(base_address=URL)
