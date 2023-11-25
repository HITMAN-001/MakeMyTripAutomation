from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture
def webdriver_obj() -> webdriver:
    Chromedriver = webdriver.Chrome(service=Service("E:\\Selenium\\chromedriver.exe"))
    Chromedriver.get("https://www.makemytrip.com/")
    Chromedriver.implicitly_wait(5)
    Chromedriver.maximize_window()
    yield Chromedriver
    Chromedriver.quit()