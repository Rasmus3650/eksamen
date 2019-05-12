import matplotlib.pyplot as plt
import matplotlib.animation as ani
from eksamen.visualize.style import PlotStyle
import random
import time


class Mergesort(object):
    def __init__(self, array):
        self.fig, self.ax = plt.subplots()
        self.arr = array
        print(self.arr)
        self.data =[[x] for x in self.arr]
        print(self.data)
        self.data.insert(0, [12])
        self.data.insert(0, [12])
        self.start()

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

    def merge_sort(self):
        start_tid = time.time()
        iter_count = 0

        while len(self.data) > 1:

            nd = []
            for i in range(len(self.data)):

                if i % 2 == 1:
                    continue
                try:
                    nd.append(self.merge(self.data[i], self.data[i + 1]))
                except IndexError:
                    nd.append(self.data.pop(-1))

                yield (i, nd, self.data, iter_count,start_tid)
            iter_count += 1
            self.data = nd

    def update(self, frame):
        ax = self.ax
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

    def start(self):
        _ = ani.FuncAnimation(self.fig, self.update, frames=self.merge_sort, repeat=False, interval=1, blit=False)
        plt.show()

