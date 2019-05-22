import matplotlib.pyplot as plt
import matplotlib.animation as ani
from eksamen.visualize.style import PlotStyle
import time
import matplotlib.tri as mtri
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas


class Quicksort():
    def __init__(self, array, start, end):
        # Vi tager imod 3 inputs, array'et der skal sorteres, start og end (start er altid 0, og end er altid længden af arrayet minus 1)
        self.array = array
        # print(self.array)
        self.start = start
        self.end = end
        self.store_end = 0
        # Vi kører funktionen der skal sortere array'et
        self.quick_sort()



    def quick_sort(self):
        if self.start < self.end:
            # Vi finder vores "pivot" som vi skal bruge senere
            pivot = self.partition(self.array,self.start,self.end)

            # Variablen store_end bliver sat til end (dette bliver relevant senere)
            self.store_end = self.end

            # ændrer på end variablen (HUSK: denne kode er afhængig af variablerne start og end's forhold til hinanden
            self.end = pivot-1

            # Kører sig selv endnu en gang med den nye end variabel
            self.quick_sort()

            # Sætter end tilbage til det den var før
            self.end = self.store_end

            # Ændrer start variablen
            self.start = pivot + 1
            # Kører sig selv med en ny start-variabel
            self.start_fun()


    def partition(self,array,start,end):
        # Vi starter med at lave to variable x og i, og de er afhængige af de parametre denne funktion tager imod
        x = array[end]
        i = start-1
        # Laver et forloop, som ittererer over tallene fra start til end+1, med en step-size på 1
        for j in range(start, end+1, 1):

             if array[j] <= x:
                 i += 1
                 if i<j:
                     z = array[i]
                     array[i] = array[j]
                     array[j] = z
             print(array)
        self.array = array

        return i

    def start_fun(self):
        self.quick_sort()

