#from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from threading import Thread
# This array 'capabilities' defines the capabilities browser, device and OS combinations where the test will run
BUILD_NAME = "browserstack-build-2"
capabilities = [
    {
        "browserName": "chrome",
        "browserVersion": "103.0",
        "os": "Windows",
        "osVersion": "11",
        "sessionName": "Parallel Test 1",  # test name
        "buildName": BUILD_NAME,  # Your tests will be organized within this build
    },
    {
        "browserName": "samsung",
        "deviceName": "Samsung Galaxy S22 Ultra",
        "osVersion": "12.0",
        "sessionName": "Parallel Test 2",
        "buildName": BUILD_NAME,
    }
]
def get_browser_option(browser):
    switcher = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
        "edge": EdgeOptions(),
        "safari": SafariOptions(),
    }
    return switcher.get(browser, ChromeOptions())

def login(driver):
    form1 = driver.find_element(By.ID, "user")
    form1.send_keys("alumno")
    form2 = driver.find_element(By.ID, "pass")
    form2.send_keys("alumnoipm")
    button = driver.find_element(By.ID,"btn")
    button.click()
    
# run_session function searches for 'BrowserStack' on duckduckgo.com
def run_session(cap):
    cap["userName"] = os.environ.get("BROWSERSTACK_USERNAME") or "brunocalabrese_dhGcyb"
    cap["accessKey"] = os.environ.get("BROWSERSTACK_ACCESS_KEY") or "Lx5zUU9x3NaaRqnsFgQc"
    options = get_browser_option(cap["browserName"].lower())
    options.set_capability("browserName", cap["browserName"].lower())
    options.set_capability("bstack:options", cap)
    driver = webdriver.Remote(
        command_executor="https://hub.browserstack.com/wd/hub", options=options
    )
    driver.get("https://tpheroku-9-8.herokuapp.com/")
    login(driver)
    driver.quit()
    
# The Thread function takes run_session function and each set of capability from the caps array as an argument to run each session parallelly
for cap in capabilities:
    Thread(target=run_session, args=(cap,)).start()
