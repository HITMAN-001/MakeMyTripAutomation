from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import  

class MakeMyTrip:
    url = 'https://www.makemytrip.com/flights/'
    def __init__(self, driver: webdriver) -> None:

        #main icons
        self.flights_button = '//*[@class="headerIcons makeFlex hrtlCenter column active"]/*[@class="chNavIcon appendBottom2 chSprite chFlights active"]'
        self.cross_button_initial = '//*[@class="commonModal__close"]'
        self.cabs_button = '//*[@class="chNavIcon appendBottom2 chSprite chCabs"]'
        self.forex_button = '//*[@class="chNavIcon appendBottom2 chSprite chForex"]'
        self.travel_insurance_button = '//*[@class="chNavIcon appendBottom2 chSprite chTravelInsurance"]'
        self.buses_button = '//*[@class="chNavIcon appendBottom2 chSprite chBuses"]'
        self.trains_button = '//*[@class="chNavIcon appendBottom2 chSprite chTrains"]'
        self.holidays_button = '//*[@class="chNavIcon appendBottom2 chSprite chHolidays"]'
        self.homestay_button = '//*[@class="chNavIcon appendBottom2 chSprite chHomestays"]'
        self.hotels_button = '//*[@class="chNavIcon appendBottom2 chSprite chHotels"]'
        self.driver = driver

        #search fields
        self.search = '//*[@class="primaryBtn font24 latoBold widgetSearchBtn "]'

        #fare types
        self.regular_fares = '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/ul/li[1]/p'
        self.armed_forces = '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/ul/li[2]/p'
        self.student_fares = '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/ul/li[3]/p'
        self.senior_sitizen = '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/ul/li[4]/p'
        self.doctors_nurses = '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/ul/li[5]/p'
        self.double_seat = '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/ul/li[6]/p'

        #get_app
        self.mobile_number = '//*[@data-test="appDownloadWrapper_input"]'
        self.get_app_button = '//*[@data-test="submitBtnWrapper"]'

        #login
        self.login_button = '//*[@data-cy="account"]'

        #flight booking paths
        self.from_city_btn = '//*[@for="fromCity"]'
        self.from_flight_text = '//*[@placeholder="From"]'
        self.to_city_btn = '//*[@for="toCity"]'
        self.to_flight_text= '//*[@placeholder="To"]'
        self.data_suggestion_index0 = '//*[@data-suggestion-index="0"]'
        self.day_picker = '//*[@aria-label="Thu Dec 21 2023"]'

    def click_regular_fare(self):
        self.driver.find_element(By.XPATH, self.regular_fares).click()

    def click_armed_forces(self):
        self.driver.find_element(By.XPATH, self.armed_forces).click()

    def click_student_fares(self):
        self.driver.find_element(By.XPATH, self.student_fares).click()

    def click_on_cross(self):
        self.driver.find_element(By.XPATH, self.cross_button_initial).click()

    def fly_from_to_city(self):
        self.driver.find_element(By.XPATH, self.from_city_btn).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.from_flight_text).send_keys("mumbai")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.data_suggestion_index0).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.to_city_btn).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.to_flight_text).send_keys("pune")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.data_suggestion_index0).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.day_picker).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.search).click()
        time.sleep(10)
    




        