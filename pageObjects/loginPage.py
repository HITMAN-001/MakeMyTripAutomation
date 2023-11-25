from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.error_messgae = '//*[@data-cy="serverError"]'
        self.continue_button = '//*[@data-cy="continueBtn"]/span[1]'
        self.user_name = '//input[@id="username"]'
        self.password = '//*[@type="password"]'
        self.submit_btn = '//*[@type="submit"]'
        self.login_button = '//*[@data-cy="account"]'
        self.error_message = '//*[@class="validity font12 redText appendTop5 makeFlex"]'

    def enter_user_name(self,*,username):
        self.driver.find_element(By.XPATH, self.user_name).send_keys(username)
    
    def enter_password(self, *, password):
        self.driver.find_element(By.XPATH, self.password).send_keys(password)

    def click_email_submit(self):
        self.driver.find_element(By.XPATH, self.continue_button).click()

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def click_password_submit(self):
        self.driver.find_element(By.XPATH, self.submit_btn).click()

    def check_for_error_message(self):
        return True if self.driver.find_element(By.XPATH, self.error_message) else False
    