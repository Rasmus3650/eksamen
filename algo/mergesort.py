#import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from visualize.style import PlotStyle
import random
import time


fig, ax = plt.subplots()

def merge(a,b):
    merged = []
    while len(a) and len(b):
        if a[0] < b[0]:
            merged.append(a.pop(0))
        else:
            merged.append(b.pop(0))
    while len(a):
        merged.append(a.pop(0))
    while len(b):
        merged.append(b.pop(0))
    return merged


def merge_sort():
    print("ggg")

    n = len(arr)
    counter = 0
    iter_count = 0
    is_sorted = False
    sub_arr = arr[0:round(n / 2)]

    data = [[x] for x in arr]


    while len(data) > 1:

        nd = []
        for i in range(len(data)):
            print(len(data))
            if i % 2 == 1:
                continue
            try:
                nd.append(merge(data[i], data[i + 1]))
            except IndexError:
                nd.append(data.pop(-1))
            yield (i, nd, data)
        data = nd
        print(data)


def animer(frame):
    datums, i, iter_count = frame
    ax.clear()
    PlotStyle.apply(ax)
    bars = ax.bar(range(len(arr)), datums)
    for k in range(len(arr)):
        if k == i+1:
            bars[k].set_color(PlotStyle.RED)
        else:
            bars[k].set_color(PlotStyle.BLUE)

    ax.set_title("Iteration number {}".format(iter_count))




arr = [random.randint(1, 1000) for i in range(int(input()))]

print(arr)

_ = ani.FuncAnimation(fig, animer, frames=merge_sort, interval=1, blit=False, repeat=False)
plt.show()