import pytest
from pageObjects.loginPage import LoginPage
from pageObjects.MakeMyTripHomePage import MakeMyTrip
from pageObjects.advertisements import Advertisement
from logs.logger_module import LogGen
logger = LogGen.loggen()


@pytest.mark.booking
def test_invalid_email(webdriver_obj):
    logger.info("Starting the test booking.")
    homepage = MakeMyTrip(driver=webdriver_obj)
    import time
    time.sleep(10)
    homepage.fly_from_to_city()