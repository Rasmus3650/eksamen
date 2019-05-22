# Her har vi en class vi har kaldt plot style og den har vi så vi nemt kan ændre hvordan vores plots ser ud
class PlotStyle:
    # Farvernes korresponderende hexværdier
    BG = '#1A463B'
    BLUE = '#35D1AA'
    RED = '#F73E5F'
    ORANGE = '#E98144'
    GREEN = '#7BC280'
    BROWN = '#B08669'

    # En staticmethod bliver brugt fordi vi ikke skal bruge andet fra vores class og den tager sig kun af dets parameter altså funktionen
    # Forskellen på en staticmethod og en class er at static ved intet om den class funktionen er inde i og bruger kun funktionen
    # En class method accesser classen, fordi at dens parametre altid er classen selv
    @staticmethod
    # Her har vi en apply funktion hvor vi fortæller den hvordan grafen skal se ud
    def apply(plot_object):
    # Har sat facecolor til BG variablen som er defineret længere oppe
        plot_object.set_facecolor(PlotStyle.BG)
    # Vi behøver ikke nogen akser på vores graf, da det er unødvendigt og det ser grimt ud
        plot_object.xaxis.set_visible(False)
        plot_object.yaxis.set_visible(False)
