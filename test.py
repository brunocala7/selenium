from importlib.resources import path
from lib2to3.pgen2 import driver
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://tpheroku-9-8.herokuapp.com/")

element = driver.find_element(by="id",value="user")


driver.close()