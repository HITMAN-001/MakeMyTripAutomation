#bring the data from excel
#how to run a test in quite mode
#add tracebacks to the log


import pytest
from pageObjects.loginPage import LoginPage
from pageObjects.MakeMyTripHomePage import MakeMyTrip
from pageObjects.advertisements import Advertisement
from logs.logger_module import LogGen
logger = LogGen.loggen()


def test_login_using_valid_email(webdriver_obj):
    #continue does not work when doing test automation
    logger.info("Starting the test script execution.")
    
    MakeMyTrip(driver=webdriver_obj).click_on_cross()
    loginpage = LoginPage(driver=webdriver_obj)
    loginpage.click_login_button()
    loginpage.enter_user_name(username=r"9545868078")
    loginpage.click_email_submit()
    loginpage.enter_password(password="xxppooo")
    loginpage.click_password_submit()


@pytest.mark.login
def test_invalid_email(webdriver_obj):
    logger.info("Starting the test invalid login.")
    loginpage = LoginPage(driver=webdriver_obj)
    import time
    time.sleep(10)
    loginpage.click_login_button()
    loginpage.enter_user_name(username=r"rohan92@gma")
    loginpage.click_email_submit()
    assert loginpage.check_for_error_message() == True

    


