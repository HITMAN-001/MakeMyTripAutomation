from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class MakeMyTrip:
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
        self.search = '//button[contains(text(),"Search")]'

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

        #flight booking buttons
        self.from_city_btn = '//*[@for="fromCity"]'
        self.from_flight_text = '//*[@placeholder="From"]'
        self.to_city_btn = '//*[@for="toCity"]'
        self.to_flight_text= '//*[@placeholder="To"]'
        self.data_suggestion_index0 = '//*[@data-suggestion-index="0"]'
        self.day_picker = '//*[@aria-label="Thu Dec 21 2023"]'

        #hotel booking buttons
        self.city_input = '//input[@data-cy="city"]'
        self.delhi_city = '//*[@class="sr_city"][1]'
        self.start_day_selected = '//*[@class="DayPicker-Day DayPicker-Day--start DayPicker-Day--selected"]'
        self.end_day_selected = '//*[@aria-label="Thu Nov 30 2023"]'
        self.rooms_drop_down = '//*[@data-testid="room_count"]'
        self.adults_drop_down = '//*[@data-testid="adult_count"]'
        self.children_count_drop_down = '//*[@data-testid="children_count"]'
        self.apply_button = '//button[contains(text(),"Apply")]'

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

    def book_hotel_in_delhi(self):
        self.driver.find_element(By.XPATH, self.hotels_button).click()
        self.driver.find_element(By.XPATH, self.city_input).click()
        self.driver.find_element(By.XPATH, self.delhi_city).click()
        start_day = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.start_day_selected)))
        start_day.click()
        self.driver.find_element(By.XPATH, self.end_day_selected).click()

        """
        rooms_selector = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.rooms_drop_down)))
        rooms = Select(rooms_selector)
        rooms.select_by_visible_text('2')

        adults_dropdown = self.driver.find_element(By.XPATH, self.adults_drop_down)
        adults = Select(adults_dropdown)
        adults.select_by_visible_text('2')

        children_dropdown = self.driver.find_element(By.XPATH, self.children_count_drop_down)
        children = Select(children_dropdown)
        children.select_by_visible_text('2')
        """
        self.driver.find_element(By.XPATH, self.apply_button).click()
        search_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.search)))
        search_btn.click()
        time.sleep(10)



        