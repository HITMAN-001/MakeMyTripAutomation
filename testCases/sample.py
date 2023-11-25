from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

Chromedriver = webdriver.Chrome(service=Service("E:\\Selenium\\chromedriver.exe"))
Chromedriver.get("https://www.makemytrip.com/")
Chromedriver.implicitly_wait(5)
Chromedriver.maximize_window()
driver = Chromedriver
cross_btn_ad = '//*[@id="webklipper-publisher-widget-container-notification-close-div"]'
time.sleep(30)
element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, cross_btn_ad)))
print(element)
element.click()