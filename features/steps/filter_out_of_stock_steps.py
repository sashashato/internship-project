from time import sleep

from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.main_page import MainPage

@given("Open the main page https://soft.reelly.io")
def open_main_page(context):
    context.app.main_page = MainPage(context.driver)
    context.app.main_page.open_main_page()

@when("Log in to the page")
def sign_in_user(context):
    context.app.login_page.sign_in(
        email='sashashatosasha@gmail.com' ,
        password='Shato@reelly91'
    )

@when("Click on “Off-plan” at the left side menu")
def click_off_plan(context):
    context.app.left_menu_page.click_off_plan()

@then ("Verify the right page opens")
def verify_off_plan_page_opens(context):
    expected_url = "https://find.reelly.io/?pricePer=unit&withDealBonus=false&handoverOnly=false&handoverMonths=1"
    sleep(2)
    WebDriverWait(context.driver, 10).until(
        EC.url_to_be(expected_url)
    )

    actual_url = context.driver.current_url
    assert actual_url == expected_url, f"Expected {expected_url}, but got {actual_url}"

@when("Filter by sale status of “Out of Stock”")
def filter_out_of_stock(context):
    context.app.off_plan_page.filter_by_out_of_stock()

@then("Verify each product contains the Out of Stock")
def verify_each_product_contains(context):
    context.app.off_plan_page.verify_all_products_out_of_stock()