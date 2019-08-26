import numpy as np
from matplotlib import pyplot as plt


def set_graph(ax, x, y, label=""):
    ax.plot(x, y, label=label)
    ax.set_xlim(-7.0, 7.0)
    ax.set_ylim(-5.0, 5.0)
    ax.grid(True)


def transfer(x):
    return np.cos(x) + 2 * np.cos(2 * x)


def rectangle_wave(x):
    ret = 0.5
    for i in range(100):
        n = i + 1
        ret += 2 / ((2 * n - 1) * np.pi) * np.sin((2 * n - 1) * x)

    return ret


def triangle_wave(x):
    T = 10
    f_t = T / 4
    f_t1 = 0

    for i in range(100):
        n = i + 1
        f_t1 += np.cos(2 * (2 * n - 1) * np.pi * x / T) / (2 * n - 1) ** 2
    f_t -= 2 * T / (np.pi * np.pi) * f_t1

    return f_t


def subtitle_1():
    fig = plt.figure()

    # 1
    ax = fig.add_subplot(221)

    # x = np.arange(-35, 35, 0.01)
    x = np.arange(-35, 35, 1)
    y = transfer(x)

    set_graph(ax, x, y, "cosx + 2cos2x")

    # 2
    ax222 = fig.add_subplot(222)

    # x1 = np.arange(-35, 35, 0.01)
    x1 = np.arange(-35, 35, 1)
    y1 = rectangle_wave(x1)

    set_graph(ax222, x1, y1, "矩形波")

    # 3
    ax223 = fig.add_subplot(223)

    # x2 = np.arange(-35, 35, 0.01)
    x2 = np.arange(-35, 35, 1)
    y2 = triangle_wave(x2)

    set_graph(ax223, x2, y2, "矩形波")

    # show
    plt.show()


if __name__ == "__main__":
    subtitle_1()

