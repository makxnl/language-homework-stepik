import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru or en-gb or es or fr")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    if language == "ru":
        print("\nstart Ru browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': "ru"})
        browser = webdriver.Chrome(options=options)
    elif language == "en-gb":
        print("\nstart en-gb browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': "en-gb"})
        browser = webdriver.Chrome(options=options)
    elif language == "es":
        print("\nstart es browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': "es"})
        browser = webdriver.Chrome(options=options)
    elif language == "fr":
        print("\nstart fr browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': "fr"})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be ru or en-gb or es or fr")
    yield browser
    print("\nquit browser..")
    browser.quit()
