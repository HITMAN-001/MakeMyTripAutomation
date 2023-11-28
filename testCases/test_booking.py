import pytest
from pageObjects.loginPage import LoginPage
from pageObjects.MakeMyTripHomePage import MakeMyTrip
from pageObjects.advertisements import Advertisement
from logs.logger_module import LogGen
logger = LogGen.loggen()


@pytest.mark.booking_flights
def test_invalid_email(webdriver_obj):
    logger.info("Starting the test booking.")
    homepage = MakeMyTrip(driver=webdriver_obj)
    homepage.fly_from_to_city()

@pytest.mark.booking_hotels
def test_hotel_booking(webdriver_obj):
    logger.info("Starting hotel booking")
    homepage = MakeMyTrip(driver=webdriver_obj)
    homepage.book_hotel_in_delhi()