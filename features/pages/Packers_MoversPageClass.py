import time
from selenium.webdriver.common.by import By


class Packers_Movers_Class:

    def __init__(self, driver):
        self.driver = driver

        self.nameTextBoxElement = "//input[@id='pnm-name']"
        self.mobile_numberTextBoxElement = "//input[@name='pnm-mobile']"

        self.relocationTextBoxElement = "//input[@id='pnm-movingfrom']"
        self.select_city_name = "(//li[@class='location__city__item'])[1]"

        self.click_Quote = "Request a Callback"
        self.Text = "//*[text()='Enter your details']"

        # invalid

        self.nameTextBoxElement = "//input[@id='pnm-name']"
        self.mobile_numberTextBoxElement = "//input[@name='pnm-mobile']"
        self.errorMsg = "//div[@id='pnm-name-error-message']"

        # bwt cities

        self.betweenCities = "//div[@class='pack-move__form-section__tab']"

        self.nameTextBoxElement = "//input[@id='pnm-name']"
        self.mobile_numberTextBoxElement = "//input[@name='pnm-mobile']"

        self.relocation2 = "//input[@class='mb-form__input location-input'][1]"
        self.relocation2_1 = "(//li[@class='location__city__item'])[41]"

        self.click_Quote = "Request a Callback"
        self.Text = "//*[text()='Enter your details']"


    # Funtionality Valid


    def enter_name(self, un):
        name = self.driver.find_element(By.XPATH, self.nameTextBoxElement)
        name.send_keys(un)

    def enter_mobile_number(self, un):
        mobile_number = self.driver.find_element(By.XPATH, self.mobile_numberTextBoxElement)
        mobile_number.send_keys(un)



    def click_relocation_from(self):
        relocation = self.driver.find_element(By.XPATH, self.relocationTextBoxElement)
        self.driver.execute_script("arguments[0].click();", relocation)

    def click_relocate_city_from(self):
        relocate_city = self.driver.find_element(By.XPATH, self.select_city_name)
        self.driver.execute_script("arguments[0].click();", relocate_city)



    def click_Request_CallBack(self):

        quotes = self.driver.find_element(By.LINK_TEXT, self.click_Quote)
        self.driver.execute_script("arguments[0].click();", quotes)
        time.sleep(5)

    def display_text(self):
        element = self.driver.find_element(By.XPATH, self.Text).is_displayed()
        return element


    # Funtionality Invalid


    def enter_invalid_name(self, un):
        name = self.driver.find_element(By.XPATH, self.nameTextBoxElement)
        name.send_keys(un)

    def enter_invalid_mobile_number(self, un):
        mobile_number = self.driver.find_element(By.XPATH, self.mobile_numberTextBoxElement)
        mobile_number.send_keys(un)

    def display_error_message(self):
        error = self.driver.find_element(By.XPATH, self.errorMsg).text
        return error


    # Between Cities (DDF)


    def select_bwt_cities(self):
        bwt_cities = self.driver.find_element(By.XPATH, self.betweenCities)
        self.driver.execute_script("arguments[0].click();", bwt_cities)


    def enter_Name(self, un):
       name = self.driver.find_element(By.XPATH, self.nameTextBoxElement)
       name.send_keys(un)

    def enter_Mobile_number(self, num):
       mobile_number = self.driver.find_element(By.XPATH, self.mobile_numberTextBoxElement)
       mobile_number.send_keys(num)



    def click_relocation_to(self):
           relocation_2 = self.driver.find_element(By.XPATH, self.relocation2)
           self.driver.execute_script("arguments[0].click();", relocation_2)

    def click_relocate_city_to(self):
           relocate_pune = self.driver.find_element(By.XPATH, self.relocation2_1)
           self.driver.execute_script("arguments[0].click();", relocate_pune)


    def click_Request_Callback(self):
           quotes = self.driver.find_element(By.LINK_TEXT, self.click_Quote)
           self.driver.execute_script("arguments[0].click();", quotes)
           time.sleep(5)

    def display_Text(self):
           element = self.driver.find_element(By.XPATH, self.Text)
           return element