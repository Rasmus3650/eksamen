import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from eksamen.visualize.style import PlotStyle
import time

iter_count = -1
x = []
start_time = time.time()
def quicksort():
    global x
    global iter_count
    iter_count += 1
    if (iter_count == 0):
        x = [0,43,21,6,2,75,4,3,5,6]
    print(x)

    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x) - 1):
            if x[j + 1] < pivot:
                x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
                i += 1
        x[0], x[i] = x[i], x[0]
        yield (x, i)
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i + 1:])
        first_part.append(x[i])
        return first_part + second_part


def animer(frame):
    global start_time
    arr = [0,43,21,6,2,75,4,3,5,6]
    fig, ax = plt.subplots()
    datums, i, = frame
    ax.clear()
    PlotStyle.apply(ax)
    bars = ax.bar(range(len(arr)), datums)
    for k in range(len(arr)):
        if k == i + 1:
            bars[k].set_color(PlotStyle.RED)
        else:
            bars[k].set_color(PlotStyle.BLUE)

    ax.set_title("Iteration number {0}  Time: {1}".format(iter_count, round(time.time() - start_time, 2)))


def start():
    fig, ax = plt.subplots()
    _ = ani.FuncAnimation(fig, animer, frames=quicksort, interval=1, blit=False, repeat=False)
    plt.show()


start()

