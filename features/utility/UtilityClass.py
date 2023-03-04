from selenium import webdriver
from features.utility.ConfigClass import ConfigClass


class UtilityClass:

    def __init__(self):
        self.driver = None

    def maximize_window(self):
        self.driver.maximize_window()

    def launch_browser(self):
        self.driver = webdriver.Chrome(ConfigClass.filePath)

    def launch_app(self):
        self.driver.get(ConfigClass.url)

    def close_browser(self):
        self.driver.quit()


