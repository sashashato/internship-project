from pages.left_menu_page import LeftMenuPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.off_plan_page import OffPlanPage

class Application:
    def __init__(self, driver):
        self.left_menu_page = LeftMenuPage(driver)
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        self.off_plan_page = OffPlanPage(driver)
