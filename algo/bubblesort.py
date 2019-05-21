import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from eksamen.visualize.style import PlotStyle
import time

#Vi har vores bubblesort class og det er sat i en class så vi nemt kan tilgå det i main.py
class Bubblesort(object):
    def __init__(self, array):
        self.fig, self.ax = plt.subplots()
        self.arr = array
        self.start()

    def bubblesort(self):
        #arrayed der skal sorteres
        arr = self.arr
        n = len(arr)
        #Counter holder styr på hvor langt i arrayed den er
        counter = 0
        #iter_count holder styr på hvor mange gange den har kørt det igennem
        iter_count = 0
        #bliver brugt til at fortælle os om arrayet er sorteret
        is_sorted = False
        #Tid så vi kan måle hvor lang tid det tog
        start_time = time.time()

        while not is_sorted:
            #For loop og det er n-1 da len() starter ikke i 0 men i en
            for i in range(n-1):
                #Hvis indeks i er større end indeks i+1
                if arr[i] > arr[i+1]:
                #så bliver de defineret til et nyt indeks altså byttet rundt
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                else:
                #Ellers så bliver counter +=1 og den går videre
                    counter += 1
                #Vi bruger yield da vi kan sende data ud af funktionen men den gemmer staten af funktionen
                #Så det er at den kan fortsætte, dette ville ikke ske hvis vi brugte return
                yield (arr, i, iter_count, start_time)
            #Hvis counter er lig med længden af arrayet
            if counter == n-1:
            #Så er det sorteret
                is_sorted = True
            else:
                #ellers bliver counter sat til 0 og iter counter += 1 og den vil køre igen da det er et while loop
                counter = 0
                iter_count += 1

    def animer(self, frame):
        arr = self.arr
        fig = self.fig
        ax = self.ax
        #Her bruger vi de variabler vi får ud af yield
        datums, i, iter_count, start_time = frame
        ax.clear()
        #Bruger den plotstyle class vi lavede
        PlotStyle.apply(ax)
        #sætter barene til længden op efter vores værdier
        bars = ax.bar(range(len(arr)), datums)
        #Her er for looped der styrer farven
        for k in range(len(arr)):
            if k == i+1:
                #Her sætter den farven til baren til at være rød
                bars[k].set_color(PlotStyle.RED)
            else:
                #Ellers forbliver den blå
                bars[k].set_color(PlotStyle.BLUE)
        #Vores titel er to counters så derfor kan vi bruge .format() og så sætte de variabler ind som vi vil have
        ax.set_title("Iteration number {0}  Time: {1}".format(iter_count, round(time.time() - start_time, 2)))

    def start(self):
        #Her siger vi at vi vil have en figur hvor vi bruger animer funktionen og bubblesort som vores frames
        #Og den skal ikke være på repeat
        _ = ani.FuncAnimation(self.fig, self.animer, frames=self.bubblesort, interval=1, blit=False, repeat=False)
        plt.show()
