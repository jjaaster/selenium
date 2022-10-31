# import webdriver
from selenium import webdriver

# run web driver
driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# add_cookie method driver
driver.add_cookie({"name" : "foo", "value" : "bar"})

# get browser cookie
driver.get_cookie("foo")


# get all cookies in scope of session
print(driver.get_cookies())

# delete browser cookie
driver.delete_cookie("foo")

# clear all cookies in scope of session
driver.delete_all_cookies()
