# import pandas as pd
# if __name__ == "__main__":
#     df_movies1=pd.read_csv("douban1.csv",encoding="utf-8")
#     print(df_movies1)
#     df_movies2=pd.resd_csv("douban1.csv",nrows=20,encoding="utf-8")
#     print(df_movies2)
#     df_movies3=pd.read_csv("douban1.csv",skipfooter = 40,encoding="utf-8")
#     print(df_movies3)
#     df_movies4 = pd.read_csv("douban1.csv", na_values=[""], skiprows=[1, 3, 5], encoding="utf-8")
#     print(df_movies4)
#     df_movies5 = pd.read_csv("douban2.csv", header=None, encoding="utf-8")
#     print(df_movies5)
#     names = ["t1", "t2", "t3", "t4", "t5", "t6", "t7", "t8", "t9"]
#     df_movies6 = pd.read_csv("douban2.csv", names=names)
#     print(df_movies6)
#     df_movies7 = pd.read_table("douban3.txt", sep=";")
#     print(df_movies7)


# import pandas as pd
# if __name__ == "__main__":
#     #读取所有数据集
#     df_movies=pd.read_csv("douban4.csv",encoding="utf-8")
#     df_movies1 = df_movies.dropna(how='all')
#     print(df_movies1)
#     df_movies2 = df_movies.dropna()
#     print(df_movies2)
#     df_movies3 = df_movies.dropna(how='all',axis=1)
#     print(df_movies3)
#     df_movies4=df_movies.dropna(axis=1)
#     print(df_movies4)
#     df_movies5 = df_movies.fillna(0)
#     print(df_movies5)
#     df_movies6=df_movies.fillna({"rating":5.0,"year":2018})
#     print(df_movies6)
#     df_movies.fillna({"rating": 5.0, "year": 2018},inplace=True)
#     print(df_movies)