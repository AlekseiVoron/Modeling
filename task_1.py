# Вариант 3
import math

import matplotlib.pyplot as plt

VESSEL_HEIGHT = 6           # высота сосуда
VESSEL_DIAMETER = 4         # диаметр сосуда
HOLE_RADIUS = 1           # радиус круглого отверстия на дне
k = 0.6                     # коэффициент скорости истечения жидкости из отверстия
g = 9.8                     # ускорение свободного падения


def circle_area(r: float):              # площадь круга
    return math.pi * r ** 2


s = circle_area(HOLE_RADIUS)             # площадь отверстия на дне сосуда
S = circle_area(VESSEL_DIAMETER / 2)     # площадь горизонтального сечения сосуда

# Требуется определить время, в течение которого уровень воды в сосуде станет
# равным 0.1 метра
RES = 0.1

h = 0.01                    # временной шаг


def f(x: float):
    return -k * s * math.sqrt(2 * g * x) / S


def euler(x, t):
    x_array.append(x)
    t_array.append(t)
    while x > RES:
        x = x + h * f(x)
        x_array.append(x)
        t = t + h
        t_array.append(t)
    return t


if __name__ == '__main__':
    print(f'Коэффициент скорости истечения жидкости из отверстия: {k}')
    print(f'Ускорение свободного падения: {g} м/с^2\n')
    print(f'Высота сосуда: {VESSEL_HEIGHT} м')
    print(f'Диаметр сосуда: {VESSEL_DIAMETER} м')
    print('В начальный момент времени сосуд дохерху наполнен водой\n')
    print(f'Площадь отверстия на дне сосуда: {s} м^2')
    print(f'Площадь горизонтального сечения сосуда: {S} м^2\n')

    x_array = []
    t_array = []
    res_time = euler(VESSEL_HEIGHT, 0)

    print(f'Уровень воды достигнет {RES} м через {round(res_time, 2)} с')

    plt.xlabel('Время, с')
    plt.ylabel('Уровень воды, м')
    plt.grid()
    plt.plot(t_array, x_array)
    plt.show()
