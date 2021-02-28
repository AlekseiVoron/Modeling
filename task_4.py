import random
import matplotlib.pyplot as plt

DOTS_1 = 50  # точек в первом испытании
DOTS_2 = 100

if __name__ == '__main__':
    values_1 = [random.random() for _ in range(DOTS_1 + 2)]
    values_2 = [random.random() for _ in range(DOTS_2 + 2)]
    xs_1 = values_1[:-2]
    ys_1 = values_1[2:]
    xs_2 = values_2[:-2]
    ys_2 = values_2[2:]
    fig, axes = plt.subplots(1, 2)
    axes[0].plot(xs_1, ys_1, 'ro', label=f'{DOTS_1} точек')
    axes[0].set_title(f'{DOTS_1} точек')
    axes[0].axis('scaled')
    axes[1].plot(xs_2, ys_2, 'bx', label=f'{DOTS_2} точек')
    axes[1].set_title(f'{DOTS_2} точек')
    axes[1].axis('scaled')
    plt.show()
