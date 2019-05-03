import matplotlib.pyplot as plt
import matplotlib.animation as ani
from visualize.style import PlotStyle
import random
import time


class Mergesort():
    fig, ax = plt.subplots()
    arr = [random.randint(1, 1000) for i in range(int(input()))]

    def merge(self, a, b):
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

    def merge_sort(self, arr, merge):
        start_tid = time.time()
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

                yield (i, nd, data, iter_count,start_tid)
            iter_count += 1
            data = nd

    def update(self, frame, ax):
        i, nd, datums, iter_count, start_tid = frame
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
        ax.set_title("Iteration number: {0}   Time: {1}".format(iter_count, round(time.time() - start_tid, 2)))
        bars = ax.bar(range(len(flat)), flat, color=colors)

    def start(self, fig, update, merge_sort):
        _ = ani.FuncAnimation(fig, update, frames=merge_sort, repeat=False, interval=1, blit=False)
        plt.show()
