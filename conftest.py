import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', default='en', help='Choose the language to test with')


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language') 
    options = Options()
    options.add_experimental_option('prefs', {
        'intl.accept_languages': language
    })
    browser = webdriver.Edge(options)
    yield browser
    browser.quit()