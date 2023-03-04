from selenium.webdriver.common.by import By

class Packers_Movers:

    def __init__(self,driver):
        self.driver = driver

    def click_packers_movers_button(self):
        self.driver.maximize_window()

        button = self.driver.find_element(By.XPATH, "//a[@class='pay-your-rent']")
        self.driver.execute_script("arguments[0].click();", button)
