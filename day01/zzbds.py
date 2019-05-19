#!/usr/bin/env python # -*- coding: UTF-8 -*- 

# @Time     : 2019/5/11 18:24 
# @Author   : 984185626@qq.com 
# @FileName : zzbds.py 
# @GitHub   : https://github.com/zhaochenjin/zp-0510 
 
import re

str="我的手机号：12345678976，你的呢？是：12345676543吗？"
phone=re.findall("\d",str)
print(phone)

phone1=re.findall("\d+",str)
print(phone1)

str2="13245676543"
phone2=re.findall("13[0-9]{9}",str2)
print(phone2)

str3="232xxixxwfraxxlovexx24r434sdfdxxyouxxsawew"
phone3=re.findall("xx.*xx",str3)
print(phone3)

phone4=re.findall("xx(.*)xx",str3)
print(phone4)

phone5=re.findall("xx(.*?)xx",str3)
print(phone5)