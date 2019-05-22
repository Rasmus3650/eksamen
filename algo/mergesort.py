import matplotlib.pyplot as plt
import matplotlib.animation as ani
from eksamen.visualize.style import PlotStyle
import random
import time


# Vi har skabt vores mergesort algoritme inde i en class, så vi nemt kan kalde den fra vores main fil
class Mergesort(object):
    #Initialize klassen
    def __init__(self, array):
        self.fig, self.ax = plt.subplots()
        # Bruger den parameter vi fik sent med
        # Putter hver enkelt værdi derfra ind i et nyt array i det store: [[1],[2],[3]...] (2D array)
        self.data = [[x] for x in array]
        # Indsætter to ligegyldige værdier ind først i arrayet
        # Dette modvirker en fejl i koden der fjernede de to første værdier
        self.data.insert(0, [12])
        self.data.insert(0, [12])
        # Kører start funktionen
        self.start()

    # Den del af algoritmen som sammenligner to eller flere tal med hinanden
    def merge(self, a, b):
        # Tomt array som vi fylder værdier i og til sidst returner
        merged = []
        # While loop der bruges til at holde øje med at der stadig er værdier i de to arrays man merger
        while len(a) and len(b):
            # Hvis a[0] er mindre end b[0] tilføj a[0] til vores merged array, og fjern den fra a
            if a[0] < b[0]:
                merged.append(a[0])
                del a[0]
            # Ellers gør det med b
            else:
                merged.append(b[0])
                del b[0]
        # Hvis der er værdier til overs, tilføjes de til sidst i arrayet
        while len(a):
            merged.append(a[0])
            del a[0]
        while len(b):
            merged.append(b[0])
            del b[0]
        # Returnere det merged array
        return merged

    # Den del af algoritmen der looper, og sørger for at sende data'ene videre
    def merge_sort(self):
        # Gemmer hvornår algoritmen starter med at køre, så vi kan se hvor længe den er igang
        start_tid = time.time()
        # Gemmer hvor mange iterations algoritmen har været igennem
        iter_count = 0

        # While loopet kører indtil der kun er 1 array tilbage i det store array, da det så må være sortet
        while len(self.data) > 1:
            # Nd er et temporary array som vi bruger til at gemme værdier i midlertidigt
            nd = []
            # For loop der kører "lengden af self.data" antal gange
            for i in range(len(self.data)):
                # Sørger for at den kun kører hver anden gang, da vi vidersender to værdier hver gang den kører
                if i % 2 == 1:
                    # Continue springer direkte videre til næste for-loop iteration
                    continue
                try:
                    # Sender to værdier videre til merge-funktionen, og putter outputtet ind i nd-arrayet
                    nd.append(self.merge(self.data[i], self.data[i + 1]))
                except IndexError:
                    # Hvis der er et ulige antal i arrayet, bliver den sidste bare tilføjet til sidst
                    # (pop returner en værdi og sletter den fra det array den blev taget fra)
                    nd.append(self.data.pop(-1))
                # Vi yielder, da det gør næsten det samme som return, den stopper bare ikke while-loopet
                yield (i, nd, self.data, iter_count,start_tid)
            # Når en iteration er færdig, plus iteration-counteren med 1
            iter_count += 1
            # Sæt vores data til at være lig med det temporary array vi lavede
            self.data = nd

    # Vores matplotlib funktion, der visualiserer det hele
    def update(self, frame):
        # Her sætter vi nogle variabler som matplotlib kræver, men også vores eget iteration-count og tiden
        ax = self.ax
        i, nd, datums, iter_count, start_tid = frame
        flat = []
        colors = []
        for k, dat in enumerate(nd):
            flat.extend(dat)
            # Her sætter vi farven på det stykke vi er ved nu til rød, og resten til blå
            # Vi ganger med lengden af vores dat variabel, ellers ville det kun være 1 bar der blev rød, og ikke alle dem vi sammenligner
            if k == len(nd) - 1:
                colors.extend([PlotStyle.RED]*len(dat))
            else:
                colors.extend([PlotStyle.BLUE]*len(dat))

        for dat in datums:
            # Vi extender flat med dat, for at sørge for at alle bars'ne er synlige, selv når det ikke er dem der bliver sammenlignet
            flat.extend(dat)
            # Vi extender colors med vores blå plotstyle, så kun dem vi sammenligner ender op med at være røde
            colors.extend([PlotStyle.BLUE]*len(dat))

        # Vi rydder axen så der er klar til at blive drawet nyt, så den ikke bare tegner ovenpå hele tiden
        ax.clear()
        # Vi applyer vores plotstyle, så den ser ud som vi vil have
        PlotStyle.apply(ax)
        # Sætter den til at vise iteration nummer, og tid, øverst (Normalt sætter man titlen 1 gang,
        # men da vi bliver ved med at køre funktionen igen kan vi komme afsted med at bruge den til at vise vores tid og iterations)
        ax.set_title("Iteration number: {0}   Time: {1}".format(iter_count, round(time.time() - start_tid, 2)))
        # Sætter barerne til vores værdier fra vores array
        bars = ax.bar(range(len(flat)), flat, color=colors)

    # Start-funktionen som kører en matplotlib funktion der kan animerer ved hjælp af en animerings funktion og en funktion der giver værdier
    def start(self):
        _ = ani.FuncAnimation(self.fig, self.update, frames=self.merge_sort, repeat=False, interval=1, blit=False)
        plt.show()
