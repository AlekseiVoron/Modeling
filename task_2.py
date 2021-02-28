import matplotlib.pyplot as plt

# граничные условия
t = 0
T = 5

h = 0.01  # шаг


def f1(x: float, a: float):
    return a * x ** 2


def f2(y: float, b: float):
    return b * y


def euler(x, y, a, b):
    global t
    i = 0
    x_array.append(x)
    y_array.append(y)
    while t < T:
        x = x + h * f1(x, a)
        y = y + h * f2(y, b)
        x_array.append(x)
        y_array.append(y)
        t = t + h
        i = i + 1


if __name__ == '__main__':
    a = float(input('a = '))
    b = float(input('b = '))
    x_0 = float(input('x_0 = '))
    y_0 = float(input('y_0 = '))

    x_array = []
    y_array = []
    euler(x_0, y_0, a, b)

    plt.title('Фазовый портрет')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.plot(x_array, y_array)
    plt.show()
