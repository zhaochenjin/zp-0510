from selenium import webdriver
import time

#声明浏览器对象
driver = webdriver.Chrome()
driver.get("https://movie.douban.com/")
a = driver.find_element_by_xpath(".//div[@class='nav-items']/ul/li[2]/a")
a.click()
time.sleep(3)

# more_button = driver.find_element_by_class_name("more")
# for i in range(5):
#     more_button.click()
#     # time.sleep(3)
#
# from lxml import etree
#
# selector = etree.HTML(driver.page_source)
# names = selector.xpath(".//div[@class='list']/a/p/text()")
# print(names)

from selenium.webdriver.common.keys import Keys # 导入Keys类

input=driver.find_element_by_id("inp-query")
input.clear()
input.send_keys("加勒比海盗")
input.send_keys(Keys.RETURN)

# driver.page_source
