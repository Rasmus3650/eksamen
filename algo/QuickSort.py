import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from eksamen.visualize.style import PlotStyle
import time


class Quicksort(object):

    def __init__(self, array):
        self.fig, self.ax = plt.subplots()
        self.arr = array
        self.iter_count = 0
        self.start_time = time.time()
        self.start()



    def quicksort(self, x):


        if len(x) == 1 or len(x) == 0:
            return x
        else:
            pivot = x[0]
            i = 0
            for j in range(len(x)-1):
                if x[j+1] < pivot:
                    x[j+1],x[i+1] = x[i+1], x[j+1]
                    i += 1
            x[0],x[i] = x[i],x[0]
            yield (x, i, self.iter_count, self.start_time)
            first_part = self.quicksort(x[:i])
            second_part = self.quicksort(x[i+1:])
            first_part.append(x[i])
            return first_part + second_part


    def animer(self, frame):
        arr = self.arr
        fig = self.fig
        ax = self.ax
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

    def start(self):
        _ = ani.FuncAnimation(self.fig, self.animer, frames=self.quicksort, interval=1, blit=False, repeat=False)
        plt.show()

