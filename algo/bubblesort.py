import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from visualize.style import PlotStyle
import time


arr = np.random.randint(1, 1000, size=int(input()))

fig, ax = plt.subplots()


def bubbleSort():
    n = len(arr)
    counter = 0
    iter_count = 0
    is_sorted = False

    start_time = time.time()

    while not is_sorted:
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                counter += 1
            yield (arr, i, iter_count, start_time)
        if counter == n-1:
            is_sorted = True
        else:
            counter = 0
            iter_count += 1


def animer(frame):
    datums, i, iter_count, start_time = frame
    ax.clear()
    PlotStyle.apply(ax)
    bars = ax.bar(range(len(arr)), datums)
    for k in range(len(arr)):
        if k == i+1:
            bars[k].set_color(PlotStyle.RED)
        else:
            bars[k].set_color(PlotStyle.BLUE)

    ax.set_title("Iteration number {0}  Time: {1}".format(iter_count, round(time.time() - start_time, 2)))

_ = ani.FuncAnimation(fig, animer, frames=bubbleSort, interval=1, blit=False, repeat=False)
plt.show()