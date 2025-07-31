from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LeftMenuPage:
    OFF_PLAN_BUTTON = (By.XPATH, "//a[@wized='newOffPlanLink']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def click_off_plan(self):
        sleep(2)
        self.wait.until(EC.presence_of_element_located(self.OFF_PLAN_BUTTON))
        elements = self.driver.find_elements(*self.OFF_PLAN_BUTTON)
        elements[0].click()
