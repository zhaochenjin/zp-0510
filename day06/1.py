import matplotlib

matplotlib.use("Agg")
import seaborn as sns

sns.set(context="notebook", style="whitegrid", palette="dark")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd  # 导入pandas科学库，读取csv文件
from sklearn.model_selection import train_test_split  # 导入sklearn科学库
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


def process_data(path):
    df = pd.read_csv(path, header=0, delimiter=",",
                     names=["DEWP", "HUMI", "PRES", "TEMP", "cbwd", "Iws", "precipitation", "Iprec", "PM25"])
    y = np.array(df.iloc[:, -1])  # 获取标签值集合
    df = df.apply(lambda column: (column - column.mean()) / column.std())
    # print("归一化后数据集:\n", df.describe())
    df.insert(0, "bais", 1)  # 增加偏置
    X = np.array(df.iloc[:, :-1])  # 获取特征值集合
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    return X_train, X_test, y_train, y_test


def test_case1(path):
    X_train, X_test, y_train, y_test = process_data(path)
    print("训练数据集:", X_train.shape, "\n", X_train[:2])
    print("测试数据集:", X_test.shape, "\n", X_test[:2])
    print("训练集标签:", y_train.shape, "\n", y_train[:2])
    print("测试集标签:", y_test.shape, "\n", y_test[:2])


if __name__ == "__main__":
    test_case1("ChengduPM2.5.csv")


def lr_cost(theta, X, y):
    m = X.shape[0]  # x.shape获取X的大小，一般为一个tuple(m,n)，其中m指行   #数，n指列数。这里我们通过下表0取行数
    inner = X @ theta - y  # 数据集X 和theta内积运算，符合矩阵乘法运算法则。#其结果取X的行数，theta的列数。然后将结果与y相减，得到误差
    square_sum = inner.T @ inner  # inner.T表示将inner转置
    cost = square_sum / (2 * m)
    return cost


def gradient(theta, X, y):
    m = X.shape[0]  #
    inner = X.T @ (X @ theta - y)
    return inner / m  # 求导过程中，分母2m被约掉了，m仍然存在，所以分母为m


def batch_gradient_decent(theta, X, y, epoch, alpha=0.01):
    initial_cost = lr_cost(theta, X, y)
    print("inital cost:%.2f" % initial_cost)
    cost_data = [initial_cost]  # 声明列表来保存迭代过程中代价函数的值
    _theta = theta.copy()  # 拷贝theta，避免和原来的theta混淆
    for i in range(1, epoch):  # epoch为迭代的批次，一批次包含全部数据的训练。例如有100万条数据，每次取10000条，要循环100次才能取完。那么一批就包含这#100次的运算。
        _theta = _theta - alpha * gradient(_theta, X, y)
        cost_value = lr_cost(_theta, X, y)
        if i % 100 == 0:
            print("第%d个100次迭代,cost=%.2f" % (int(i / 100), cost_value))
        cost_data.append(cost_value)  # 保存迭代过程中代价函数值
    return _theta, cost_data


def predict_evaluate(theta, X_test, y_test):
    y_p = X_test @ theta.T
    m = X_test.shape[0]
    return np.sum((y_p - y_test) ** 2) / m


def test_case2(path):
    X_tain, X_test, y_train, y_test = process_data(path)
    alpha = 0.01  # 学习率初值，是个经验值可以选择0.001、0.1等
    theta = np.zeros(X_tain.shape[1])  # 初始化theta的值0，个数取决于训练集特征个数。如这里每条数据由9个特征，那么theta的值为一个1行9列的向量
    epoch = 5000  # 迭代次数初值，是个经验值也可以选择1000,10000等
    final_theta, _ = batch_gradient_decent(theta, X_tain, y_train, epoch, alpha=alpha)
    print("final_theta:\n", final_theta)
    mse = predict_evaluate(final_theta, X_test, y_test)
    print("mse:", mse)  # 输出平均误差


def plot_cost_data(costs):
    sns.tsplot(time=np.arange(len(costs)), data=costs)
    plt.xlabel('epoch', fontsize=18)
    plt.ylabel('cost', fontsize=18)
    plt.savefig("epoch_cost.png")
    plt.show()


def plot_learning_rate(X, y, epoch=2000):
    base = np.logspace(-1, -5, num=3)
    candidate = np.sort(np.concatenate((base, base * 3)))
    print(candidate)
    theta = np.zeros(X.shape[1])
    fig, ax = plt.subplots(figsize=(10, 6))
    for alpha in candidate:
        _, cost_data = batch_gradient_decent(theta, X, y, epoch, alpha=alpha)
        ax.plot(np.arange(epoch), cost_data, label=alpha)
    ax.set_xlabel('epoch', fontsize=18)
    ax.set_ylabel('cost', fontsize=18)
    ax.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
    ax.set_title('learning rate', fontsize=18)
    plt.savefig("epoch_cost_rate.png")
    plt.show()


def test_case3(path):
    X_tain, X_test, y_train, y_test = process_data(path)
    alpha = 0.01
    theta = np.zeros(X_tain.shape[1])
    epoch = 2000
    final_theta, cost_data = batch_gradient_decent(theta, X_tain, y_train, epoch, alpha=alpha)
    plot_cost_data(cost_data)
    plot_learning_rate(X_tain, y_train)
