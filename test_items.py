import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_button_on_page(browser):
    browser.get(link)
    time.sleep(30)
    btn = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert btn, "Button not find"
