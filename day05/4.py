import numpy as np


def get_cost(theta,x,y):
    """
    :param theta: 矩阵
    :param x: 矩阵
    :param y: 矩阵
    :return: 矩阵
    """
    return np.sum((np.dot(x, theta) - y) ** 2)


x=np.array([[1,2],[1,2]])
y=np.array([0,0])
theta=np.array([1,1])
print(get_cost(theta,x,y))

