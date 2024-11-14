import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Language for the browser")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("--language")
    options = Options()
    options.add_argument(f"--lang={language}")
    options.add_argument(f"--accept-language={language}")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()