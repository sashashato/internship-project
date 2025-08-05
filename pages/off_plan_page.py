# from time import sleep
#
# from pages.base_page import Page
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
#
# class OffPlanPage(Page):
#     SALE_STATUS_FILTER = (By.XPATH, "//button[text()='Sale Status']")
#     OUT_OF_STOCK_OPTION = (By.XPATH, "//div[text()='Out of Stock']")
#     LOGO = (By.XPATH, "//img[@alt='logo']")
#     PRODUCT_LABELS = (By.XPATH, "//span[text()='Out of stock']")
#     MOBILE_EMPTY_PLACE = (By.XPATH, "//button[@data-state='open']")
#     # MOBILE_EMPTY_PLACE = (By.XPATH, "//*[contains(@class,'bg-black/80')]")
#
#     def filter_by_out_of_stock(self):
#         sleep(2)
#         self.wait.until(EC.element_to_be_clickable(self.SALE_STATUS_FILTER)).click()
#         self.wait.until(EC.element_to_be_clickable(self.OUT_OF_STOCK_OPTION)).click()
#         # self.wait.until(EC.element_to_be_clickable(self.LOGO)).click()
#         sleep(2)
#         self.wait.until(EC.element_to_be_clickable(self.MOBILE_EMPTY_PLACE)).click()
#
#         sleep(2)
#         self.wait.until(EC.element_to_be_clickable(self.MOBILE_EMPTY_PLACE)).click()
#         # elements = self.driver.find_elements(*self.MOBILE_EMPTY_PLACE)
#         # elements[0].click()
#
#     def verify_all_products_out_of_stock(self):
#         sleep(2)
#         elements = self.driver.find_elements(*self.PRODUCT_LABELS)
#         assert len(elements) > 0, "No products with 'Out of Stock' label found"


from time import sleep

from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionBuilder


class OffPlanPage(Page):
    SALE_STATUS_FILTER = (By.XPATH, "//button[text()='Sale Status']")
    OUT_OF_STOCK_OPTION = (By.XPATH, "//div[text()='Out of Stock']")
    LOGO = (By.XPATH, "//img[@alt='logo']")
    PRODUCT_LABELS = (By.XPATH, "//span[text()='Out of stock']")
    MOBILE_EMPTY_PLACE = (By.XPATH, "//*[contains(@class,'bg-black/80')]")

    def filter_by_out_of_stock(self):
        sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.SALE_STATUS_FILTER)).click()
        self.wait.until(EC.element_to_be_clickable(self.OUT_OF_STOCK_OPTION)).click()

    def verify_all_products_out_of_stock(self):
        sleep(2)

        # Try the mobile empty place click first (works for local)
        try:
            self.wait.until(EC.element_to_be_clickable(self.MOBILE_EMPTY_PLACE)).click()
            sleep(1)
            elements = self.driver.find_elements(*self.PRODUCT_LABELS)
            assert len(elements) > 0, "No products with 'Out of Stock' label found"
        except Exception:
            # If that fails, try the coordinate-based click (for BrowserStack)
            try:
                window_size = self.driver.get_window_size()
                x = window_size['width'] // 2
                y = window_size['height'] // 3

                actions = ActionBuilder(self.driver)
                pointer = actions.pointer_action
                pointer.move_to_location(x, y)
                pointer.click()
                actions.perform()
                sleep(1)
                elements = self.driver.find_elements(*self.PRODUCT_LABELS)
                assert len(elements) > 0, "No products with 'Out of Stock' label found"
            except Exception as e:
                raise Exception(f"Failed to perform click action: {str(e)}")