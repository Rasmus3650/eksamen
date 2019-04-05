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
            merged.append(a[0])
            del a[0]
        else:
            merged.append(b[0])
            del b[0]
    while len(a):
        merged.append(a[0])
        del a[0]
    while len(b):
        merged.append(b[0])
        del b[0]
    return merged


def merge_sort():
    iter_count = 0
    data = [[x] for x in arr]

    while len(data) > 1:

        nd = []
        for i in range(len(data)):

            if i % 2 == 1:
                continue
            try:
                nd.append(merge(data[i], data[i + 1]))
            except IndexError:
                nd.append(data.pop(-1))

            yield (i, nd, data, iter_count)
        iter_count += 1
        data = nd




def update(frame):
    i, nd, datums, iter_count = frame

    flat = []
    colors = []
    for k, dat in enumerate(nd):
        flat.extend(dat)
        if k == len(nd) - 1:
            # Differentiate the section currently
            # being merged
            colors.extend([PlotStyle.RED]*len(dat))
        else:
            colors.extend([PlotStyle.BLUE]*len(dat))

    for dat in datums:
        flat.extend(dat)
        colors.extend([PlotStyle.BLUE]*len(dat))

    ax.clear()
    PlotStyle.apply(ax)
    ax.set_title("Iteration number {}".format(iter_count))
    bars = ax.bar(range(len(flat)), flat, color=colors)

arr = [random.randint(1, 1000) for i in range(int(input()))]




_ = ani.FuncAnimation(fig, update, frames=merge_sort, repeat=False, interval=1, blit=False)
plt.show()



