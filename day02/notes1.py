#!/usr/bin/env python # -*- coding: UTF-8 -*-

# @Time     : 2019/5/13 10:19 
# @Author   : 984185626@qq.com 
# @FileName : notes1.py
# @GitHub   : https://github.com/zhaochenjin/zp-0510 
 
import requests
from lxml import etree

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}

#Session对象，模拟服务器端的Session
session=requests.Session()

url="http://accounts.douban.com/j/mobile/login/basic" # 提交表单的URL
data={
    "ck":"",
    "name":"13776097761",
    "password":"zhangtao",
    "remember":"true",
    "ticket":""
}

result = session.get(url, data=data, headers = header)
# result=session.post(url,data=data,headers=header)
print(result.text)
result=result.json() # 转换为python的字典格式
#登陆成功
# if result["status"]==True:
html = session.get("https://www.douban.com/people/168443006/notes",headers=header)
print("zxc")
# print(html.text)