import requests
from lxml import etree
import re

def parse(url):

    html = requests.get(url) # 得到HMTL文档

    selector = etree.HTML(html.text)

    all_movies = []

    movies_list = selector.xpath("//ol[@class='grid_view']/li")
    for movie_selector in movies_list:
        name = movie_selector.xpath(".//div[@class='hd']/a/span[1]/text()")[0]#名称

        star = movie_selector.xpath(".//div[@class='star']/span[@class='rating_num']/text()")[0]#评分

        nums = movie_selector.xpath(".//div[@class='star']/span[last()]/text()")[0]#人数
        # nums = nums.split("人评价")[0]
        # nums=re.findall("\d+",nums)[0]
        nums=re.sub("\D","",nums) # re.sub：用于替换字符串中的匹配项，返回替换值。

        url = movie_selector.xpath(".//div[@class='hd']/a/@href")[0] # 照片地址

        director_and_act = movie_selector.xpath(".//div[@class='bd']/p[1]/text()")[0].strip("\n").strip(" ")
        director = re.findall("导演: (.*?) ", director_and_act)[0]
        act = re.findall("主演: (.*?) ", director_and_act)
        if not act:
            act=["未知"]
        # print(act[0])
        # act=act[0]
        one_movie = [name,star,nums,url,director,act[0]]

        all_movies.append(one_movie)

    print(all_movies)

    for movie in all_movies:
        one_str = movie[0]+","+movie[1]+","+movie[2]+","+movie[3]+","+movie[4]+","+movie[5]+"\n"
        with open("movies.txt","a",encoding="utf-8") as f:
            f.write(one_str)

    next_url = selector.xpath("//span[@class='next']/a/@href")
    if next_url:
        next_url = "https://movie.douban.com/top250"+next_url[0]
        parse(next_url)

if __name__ == "__main__":
    parse("https://movie.douban.com/top250")


# img = selector.xpath('//div[@class="simple_table_nonFashion"]/div[@class="proImg"]/a[@class="img"]/text()')
# price = selector.xpath('//div[@class="simple_table_nonFashion"]/p[@class="proPrice"]/a[@class="img"]/text()')
# name = selector.xpath('//div[@class="simple_table_nonFashion"]/p[@class="proName clearfix"]/a[@class="img"]/text()')
# name = selector.xpath('//div[@class="simple_table_nonFashion"]/div[@class="proImg/a[@class="img"]/text()')


