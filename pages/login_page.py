from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

from pages.base_page import Page
from selenium.webdriver.common.by import By

class LoginPage(Page):
    EMAIL_FIELD = (By.ID, "email-2")
    PASSWORD_FIELD = (By.ID, "field")
    SIGN_IN_BTN = (By.XPATH, "//a[@wized='loginButton']")

    def open_sign_in_page(self):
        self.open_url("https://soft.reelly.io/sign-in")

    def sign_in(self, email, password):
        sleep(2)
        self.input_text(self.EMAIL_FIELD, email)
        sleep(2)
        self.input_text(self.PASSWORD_FIELD, password)
        sleep(2)
        self.click(self.SIGN_IN_BTN)

