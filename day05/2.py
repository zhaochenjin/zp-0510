def get_grad(theta, x, y):
    grad = 2 * (theta * x - y) * x  # 梯度
    return -grad


def get_cost(theta, x, y):
    return (theta * x - y) ** 2


def gradient_descending(theta, x, y, leaning_rate):
    for i in range(10):
        theta = theta + get_grad(theta, x, y) * leaning_rate
        print(theta)
        print(get_cost(theta, x, y))
        print("....................")
    return theta


y = 20
x = 1.1
theta = 0
learning_rate = 0.1
gradient_descending(theta, x, y, learning_rate)
