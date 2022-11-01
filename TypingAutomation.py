from itertools import dropwhile
from lib2to3.pgen2 import driver
import time
from webbrowser import Chrome
from Selenium import webdriver
#from Selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')

driver.implicitly_wait(10)

#driver.maximize_window

driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("testing1 tseting2 testing3")
driver.find_element_by_name("btnK").click()
driver.close()