import requests
from lxml import etree
import re
import pymongo

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

db_client=None
db_collection = None

def initMongoDB():
    global db_client
    global db_collection

    # 连接MongoDB数据库服务器
    db_client=pymongo.MongoClient()
    # 指定操作数据库的对象
    db=db_client["douban"]
    # 指定集合（类似MYSQL中的表)
    db_collection=db["movies"]


def parse(url):
    global db_cursor
    #得到HMTL文档
    html = requests.get(url,headers=header)

    #解析文档
    #获取豆瓣top250中页面的标题
    selector = etree.HTML(html.text)

    movies_list = selector.xpath("//ol[@class='grid_view']/li")
    for movie_selector in movies_list:
        name = movie_selector.xpath(".//div[@class='hd']/a/span[1]/text()")[0]#名称
        star = movie_selector.xpath(".//div[@class='star']/span[@class='rating_num']/text()")[0]#评分
        nums = movie_selector.xpath(".//div[@class='star']/span[last()]/text()")[0]#人数
        nums = re.sub("\D","",nums)
        director_and_act = movie_selector.xpath(".//div[@class='bd']/p[1]/text()")[0].strip("\n").strip(" ")
        director = re.findall("导演: (.*?) ",director_and_act)[0]
        act = re.findall("主演: (.*?) ",director_and_act)
        if not act:
            act = ["未知"]

        global db_collection
        # 插入一个文档到集合中
        one_movie={"name":name,
                    "star":star,
                    "nums":nums,
                    "director":director,
                    "act":act}
        # 插入数据库到文档
        db_collection.insert_one(one_movie)

        url = movie_selector.xpath(".//div[@class='hd']/a/@href")[0]

    next_url = selector.xpath("//span[@class='next']/a/@href")
    if next_url:
        next_url = "https://movie.douban.com/top250"+next_url[0]
        parse(next_url)

if __name__ == "__main__":
    initMongoDB()
    parse("https://movie.douban.com/top250")
    db_client.close()# 关闭数据库服务器

