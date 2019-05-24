def get_grad(theta, x, y):
    grads = 2 * (theta * x - y) * x  # 梯度
    return -grads


def get_cost(theta, x, y):
    return (theta * x - y) ** 2


def gradient_descending(theta, x, y, leaning_rate):
    theta = theta + get_grad(theta, x, y) * leaning_rate  # θ
    return theta


y = 20
x = 1.1
theta = 0
learning_rate = 0.1

theta=gradient_descending(theta, x, y, learning_rate)
cost=get_cost(theta,x,y)
print(cost)
print(theta)

theta=gradient_descending(theta,x,y,learning_rate)
cost=get_cost(theta,x,y)
print(cost)
print(theta)