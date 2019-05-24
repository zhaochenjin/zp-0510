# -*- coding:utf-8 -*-
"""
读取数据
"""
import pandas as pd
import numpy as np


def read_aqi():
    aqi_data = pd.read_csv("aqi2.csv")
    cols=['PM2.5', 'PM10', 'CO', 'No2', 'So2', 'O3']
    label = aqi_data["AQI"].values.reshape(-1,1) # 转变成一列
    x=aqi_data[cols]
    x = x.apply(lambda data: np.log(data), axis=0).values
    # x = (x-np.min(x))/(np.max(x)-np.min(x))  # 数据标准化
    # 将数据拆分成3个部分，训练集占60%，验证集占30%，测试集占10%
    rows=len(x)
    train_rows=int(rows*0.6)
    validation_rows=int(rows*0.3)
    train_x,train_y=x[0:train_rows],label[0:train_rows]
    validation_x,validation_y=x[train_rows:train_rows+validation_rows],label[train_rows:train_rows+validation_rows]
    test_x,text_y=x[train_rows+validation_rows:],label[train_rows+validation_rows:]
    return (train_x,train_y),(validation_x,validation_y),(test_x,text_y)
    # return x.reshape(-1, 6), label.reshape(-1, 1)
    # 转换成六列  转换成一列


# x,y=read_aqi()
# print(x)

def standard_data(input):
    """
    对输入的数据进行标准化
    """
    return np.log(input)
