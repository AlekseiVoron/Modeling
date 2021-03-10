import random
import math
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace

N = 1000  # число частиц
LMBD = 3  # лямбда


def puasson():
    return -1 / LMBD * math.log(random.random())


def get_intervals(temp_list: list) -> list:
    return [abs(temp_list[_i + 1] - temp_list[_i]) for _i in range(len(temp_list) - 1)]


def calc_intervals_range(stream: list) -> dict:
    max_x = max(stream)
    intervals = {}
    for interval_end in linspace(0, max_x, 21)[1:]:  # нулевой интервал следует выбросить
        intervals[interval_end] = []

    for x in stream:
        for interval in intervals:
            if x <= interval:
                intervals[interval].append(x)
                break

    return intervals


def calc_frequencies(intervals: dict, count_intervals: int) -> dict:
    frequencies = {}
    for interval, dots in intervals.items():
        frequencies[interval] = len(dots) / count_intervals

    return frequencies


if __name__ == '__main__':
    t = 0
    first = []
    second = []
    for i in range(N):
        if random.random() <= 0.75:
            first.append(t)  # 3/4 частиц - в первый поток
        else:
            second.append(t)
        t += puasson()
    xs = get_intervals(first)
    ys = get_intervals(second)
    xs_len = len(xs)
    ys_len = len(ys)

    first_intervals = calc_intervals_range(xs)
    second_intervals = calc_intervals_range(ys)

    first_freqs = calc_frequencies(first_intervals, xs_len)
    second_freqs = calc_frequencies(second_intervals, ys_len)

    fig, axes = plt.subplots(2, 1)

    axes[0].bar(first_freqs.keys(), first_freqs.values(), width=0.2)
    axes[1].bar(second_freqs.keys(), second_freqs.values(), width=0.2)

    axes[0].set_title('Первый поток')
    axes[1].set_title('Второй поток')

    fig.set_facecolor('floralwhite')
    fig.set_figwidth(12)  # ширина Figure
    fig.set_figheight(6)  # высота Figure

    plt.show()
