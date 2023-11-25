from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Advertisement:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.cross_btn_ad = '//*[@class="wewidgeticon we_close"]'

    def close_ad1(self):
        try:

            element = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(By.XPATH, self.cross_btn_ad))
            self.driver.execute_script("arguments[0].click();", element)
            self.logger.info(f"element loctaed {element}")
            self.logger.info("advertisement found and closed.")
        except Exception as e:
            self.logger.info("No advertisement found.")
        