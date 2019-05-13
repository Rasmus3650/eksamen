import matplotlib.pyplot as plt
import matplotlib.animation as ani
from eksamen.visualize.style import PlotStyle
import time
import matplotlib.tri as mtri
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas


class Quicksort():
    def __init__(self,array, start, end):
        self.array = array
        #print(self.array)
        self.start = start
        self.end = end
        self.store_end = 0
        self.quick_sort()



    def quick_sort(self):
        if self.start < self.end:
            #print(self.array,self.start,self.end)
            pivot = self.partition(self.array,self.start,self.end)
            self.store_end = self.end
            self.end = pivot-1
            self.quick_sort()
            self.end = self.store_end
            self.start = pivot + 1
            self.runOnce = 0
            self.start_fun()
            """
            for i in range(len(self.array) - 1):
                plt.plot(x=i + 1, ymin=0, ymax=self.array[i])
                print(i)
            plt.axis([0, len(self.array) + 1, 0, self.array[-1]])
            plt.show()
            """

    def partition(self,array,start,end):
        x = array[end]
        i = start-1
        for j in range(start, end+1, 1):
             print(array)
             if array[j] <= x:
                 i += 1
                 if i<j:
                     z = array[i]
                     array[i] = array[j]
                     array[j] = z
        self.array = array
        #print(self.array, self.start, self.end)

        return i

    def start_fun(self):
        self.quick_sort()

