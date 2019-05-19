from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys # 导入Keys类
from lxml import etree
import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456')
cursor = db.cursor()
sql_drop = 'drop table if exists exam.yhd;'
sql_create = 'create table if not exists exam.yhd(name varchar(240) ,price varchar(20), store varchar(100) , judge varchar(40));'

cursor.execute(sql_drop)
cursor.execute(sql_create)

driver = webdriver.Chrome()
driver.get("https://www.yhd.com/")

input=driver.find_element_by_id("keyword")
input.clear()
input.send_keys("iphone")
input.send_keys(Keys.RETURN)


jsa ="window.scrollTo(0, document.body.scrollHeight-900)"
jsb ="window.scrollTo(0, document.body.scrollHeight-1000)"
driver.execute_script(jsa)
time.sleep(1)
driver.execute_script(jsb)
time.sleep(1)
driver.execute_script(jsb)

selector = etree.HTML(driver.page_source)

for i in range(1):
    for j in range(60):
        # 名称、价格、好评率、店铺名称。
        name = selector.xpath("//p[@class='proName clearfix']/a/text()")[j+1]
        price = selector.xpath(".//p[@class='proPrice']/em/text()")[j+1]
        store = selector.xpath(".//span[@class='shop_text']/text()")[j+1]
        judge = selector.xpath(".//p[@class='proPrice']/span[@class='positiveRatio']/text()")[j+1]
        print(name)
        print(price)
        print(store)
        print(judge)
        print(j)
        print("......................................")
        sql = 'INSERT INTO exam.yhd(name, price, store, judge) values(%s, %s, %s, %s)'
        try:
            cursor.execute(sql, (str(name).strip(), str(price).strip(), str(store).strip(), str(judge).strip()))
            db.commit()
        except:
            db.rollback()
        # db.close()

    # price(str(i)+' is time')
    pagenext_button = driver.find_element_by_xpath(".//a[@class='page_next']")
    pagenext_button.click()
    print('next page is ',end='')
    print(i)
    jsa = "window.scrollTo(0, document.body.scrollHeight-900)"
    jsb = "window.scrollTo(0, document.body.scrollHeight-1000)"
    driver.execute_script(jsa)
    # time.sleep(1)
    driver.execute_script(jsb)
    driver.execute_script(jsb)
    selector = etree.HTML(driver.page_source)

db.close()