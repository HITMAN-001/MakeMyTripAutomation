from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
import time

@pytest.fixture
def webdriver_obj() -> webdriver:
    Chromedriver = webdriver.Chrome(service=Service("E:\\Selenium_with_python\\chromedriver.exe"))
    Chromedriver.get("https://www.makemytrip.com/")
    Chromedriver.implicitly_wait(5)
    Chromedriver.maximize_window()
    time.sleep(5)
    yield Chromedriver
    Chromedriver.quit()