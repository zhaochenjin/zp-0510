from selenium import webdriver
import time
import requests
from lxml import etree


#声明浏览器对象
driver = webdriver.Chrome()
driver.get("https://movie.douban.com/top250/")

all_movies = {}

for i in range(10):
    movie_selector = etree.HTML(driver.page_source)
    for b in  range(25):
        name = movie_selector.xpath(".//div[@class='hd']/a/span[1]/text()")[b]  # 名称
        star = movie_selector.xpath(".//div[@class='star']/span[@class='rating_num']/text()")[b]  # 评分
        all_movies[name] = star
    if(i < 9):
        a = driver.find_element_by_xpath(".//span[@class='next']/a")
        a.click()

with open("ty.txt", "a", encoding="utf-8") as f:
    for key in all_movies:
        f.write(key+all_movies.get(key)+'\n')

# print(len(all_movies))
