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
from selenium.webdriver.support.ui import WebDriverWait
from threading import Thread
# This array 'capabilities' defines the capabilities browser, device and OS combinations where the test will run
BUILD_NAME = "browserstack-build-2"
capabilities = [
    {
        "browserName": "chrome",
        "browserVersion": "104.0",
        "os": "Windows",
        "osVersion": "7",
        "sessionName": "BStack Python sample parallel", # test name
        "buildName": BUILD_NAME,  # Your tests will be organized within this build
    },
    {
        "browserName": "firefox",
        "browserVersion": "104.0 beta",
        "os": "Windows",
        "osVersion": "11",
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

def loginMal(driver):
    form1 = driver.find_element(By.ID, "user")
    form1.send_keys("pepito")
    form2 = driver.find_element(By.ID, "pass")
    form2.send_keys("pepas")
    button = driver.find_element(By.ID,"btn")
    button.click()
    myElem = WebDriverWait(driver, 5).until(EC.alert_is_present())
    driver.switchTo().alert().accept()


def login(driver):
    driver.save_screenshot('screenshots1.png')


    form1 = driver.find_element(By.ID, "user")
    form1.send_keys("alumno")
    form2 = driver.find_element(By.ID, "pass")
    form2.send_keys("alumnoipm")
    button = driver.find_element(By.ID,"btn")
    button.click()

def formulario(driver):
    button = driver.find_element(By.ID,"nav1")
    button.click()
    form1 = driver.find_element(By.ID, "nombre")
    form1.send_keys("Pablo")
    form2 = driver.find_element(By.ID, "apellido")
    form2.send_keys("Henriquez")
    form3 = driver.find_element(By.ID, "dni")
    form3.send_keys("1037892039")
    form4 = driver.find_element(By.ID, "telefono")
    form4.send_keys("8530753790")

    driver.save_screenshot('screenshots2.png')


    boton = driver.find_element(By.ID, "boton")
    boton.click()

def navegar(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    buttuns = driver.find_element(By.ID,"nav2")
    buttuns.click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    
    buto = driver.find_element(By.ID,"nav3")
    buto.click()

    
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
    driver.get("https://pagina-final3.herokuapp.com/")
    driver.maximize_window()
    myElem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'btn')))
    login(driver)
    myElem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'boton')))
    formulario(driver)
    navegar(driver)
    myElem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'btn')))
    loginMal(driver)
    driver.quit()
    
# The Thread function takes run_session function and each set of capability from the caps array as an argument to run each session parallelly
for cap in capabilities:
    Thread(target=run_session, args=(cap,)).start()
