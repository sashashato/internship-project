from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class OffPlanPage(Page):
    SALE_STATUS_FILTER = (By.XPATH, "//button[text()='Sale Status']")
    OUT_OF_STOCK_OPTION = (By.XPATH, "//div[text()='Out of Stock']")
    LOGO = (By.XPATH, "//img[@alt='logo']")
    PRODUCT_LABELS = (By.XPATH, "//span[text()='Out of stock']")

    def filter_by_out_of_stock(self):
        self.wait.until(EC.element_to_be_clickable(self.SALE_STATUS_FILTER)).click()
        self.wait.until(EC.element_to_be_clickable(self.OUT_OF_STOCK_OPTION)).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGO)).click()

    def verify_all_products_out_of_stock(self):
        elements = self.driver.find_elements(*self.PRODUCT_LABELS)
        assert len(elements) > 0, "No products with 'Out of Stock' label found"
