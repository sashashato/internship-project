from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application
from selenium.webdriver.edge.options import Options



def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    # # # Firefox
    # options = FirefoxOptions()
    # options.add_argument('--headless')
    # options.add_argument('--width=1920')
    # options.add_argument('--height=1080')
    # service = FirefoxService()
    # context.driver = webdriver.Firefox(service=service, options=options)

    # # # Chrome
    # options = ChromeOptions()
    # options.add_argument('--headless=new')
    # options.add_argument('--window-size=1920,1080')
    # driver_path = ChromeDriverManager().install()
    # service = ChromeService(driver_path)
    # context.driver = webdriver.Chrome(service=service, options=options)


    ## BROWSERSTACK ###
    bs_user ='oleksandrashatok_Mn5JFD'
    bs_key = 'rhnm3RD19M7hHwrmKjGw'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        "os" : "Windows",
        "osVersion" : "11",
        'browserName': 'Edge',
        'sessionName': scenario_name,
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
