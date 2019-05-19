from selenium import webdriver
import time

#声明浏览器对象
driver = webdriver.Chrome()
driver.get("https://www.icourse163.org/home.htm?userId=1145423579#/home/course")
a = driver.find_element_by_xpath(".//a[@class='f-f0 navLoginBtn']")
a.click()
time.sleep(2)
a = driver.find_element_by_xpath(".//a[@class='tab0']")
a.click()
time.sleep(1)
