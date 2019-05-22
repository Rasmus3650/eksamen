########## Imports ##########

import sys
import os
import random
import pyperclip
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import *
# Importerer klasser fra vores andre filer
from eksamen.algo.mergesort import Mergesort
from eksamen.algo.bubblesort import Bubblesort
from eksamen.algo.QuickSort import Quicksort
from eksamen.algo.NeuralNetwork21 import NeuralNetwork21
from eksamen.algo.NeuralNetwork221 import OurNeuralNetwork


########## Ui til Py ##########
# Åbner gui-filen som read
fin = open("gui.ui", 'r')
# Åbner eller skaber gui.py-filen som write
fout = open("gui.py", 'w')
# Bruger PyQt's compileUi til at convertere indholdet fra indput-filen til py og sender det til output-filen
uic.compileUi(fin, fout, execute=False)
# Lukker filerne igen
fin.close()
fout.close()
###############################

# Importere gui-klassen
from eksamen.gui import Ui_MainWindow

###############################


########## Main klasse ##########
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # Initialize klassen
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        # Array som vi sender videre til sortering
        self.array = []
        self.setupUi(self)
        # Skjuler fixed array framet, sådan at det ikke ligger oven i random array
        self.fixedRadioFrame.hide()
        # Sørger for at random array er valgt
        self.radioRandom.setChecked(True)
        # Validator til at sørge for man ikke kan lave et random array der er større end 999
        validator1 = QIntValidator(0, 999, self)
        # Validator til at sørge for at neural networks ikke går over 1.000.000 iterations
        validator2 = QIntValidator(0, 1000000, self)
        # Sætter validator på line-edits'ne
        self.arrayLengthEdit.setValidator(validator1)
        self.neuralLineEdit.setValidator(validator2)
        # Sætter alle knapper til at connecte til deres funktioner
        self.radioRandom.toggled.connect(self.radiohide)
        self.radioFixed.toggled.connect(self.radiohide)
        self.randomizeArrayButton.clicked.connect(self.randomarray)
        self.mergeSortButton.clicked.connect(self.mergesortarray)
        self.bubbleSortButton.clicked.connect(self.bubblesortarray)
        self.copyClipboardButton.clicked.connect(self.copyclipboard)
        self.openFileButton.clicked.connect(self.openfilearray)
        self.quickSortButton.clicked.connect(self.quicksortarray)
        self.neuralButton21.clicked.connect(self.neural21)
        self.neuralButton221.clicked.connect(self.neural221)

    # Funktion til at skjule/vise fixed/random array frames
    def radiohide(self):
        # Hvis random array radio-knappen er valgt, vis random og skjul fixed
        if self.radioRandom.isChecked():
            self.randomRadioFrame.show()
            self.fixedRadioFrame.hide()
        # Gør det modsatte af ovenover
        else:
            self.randomRadioFrame.hide()
            self.fixedRadioFrame.show()

    # Skab et random array
    def randomarray(self):
        # Tjekker at der står et tal i line-edit og at værdien er over 1
        if self.arrayLengthEdit.text() != "" and int(self.arrayLengthEdit.text()) > 1:
            # Skaber et array med tal mellem 1 og 1000 for x antal gange, x er det tal man skrev i line-edit
            self.array = [random.randint(1, 1000) for i in range(int(self.arrayLengthEdit.text()))]
            # Gør så brugeren kan se at deres array er sat
            self.randomizedLabel.setText("Randomized")
        else:
            # Ændre på teksten så brugeren kan se at de har gjort noget forkert
            self.randomizedLabel.setText("Choose a value above 1")

    ###### De tre funktioner som kalder de tre sorts, tjek at array ik er tomt ######
    def mergesortarray(self):
        if len(self.array) > 0:
            Mergesort(self.array)
        else:
            self.randomizedLabel.setText("You need an array")

    def bubblesortarray(self):
        if len(self.array) > 0:
            Bubblesort(self.array)
        else:
            self.randomizedLabel.setText("You need an array")

    def quicksortarray(self):
        if len(self.array) > 0:
            Quicksort(self.array, 0, len(self.array) - 1)
        else:
            self.randomizedLabel.setText("You need an array")
    ##################################################################################

    ###### De to funktioner som kalder de to neural, tjek at iterations er over 0 ######
    def neural21(self):
        if self.neuralLineEdit.text() != "":
            # Set iterations til værdi fra line-edit
            self.iter = int(self.neuralLineEdit.text())
            if self.iter > 0: NeuralNetwork21(self.iter)

    def neural221(self):
        if self.neuralLineEdit.text() != "":
            # Set iterations til værdi fra line-edit
            self.iter = int(self.neuralLineEdit.text())
            if self.iter > 0: OurNeuralNetwork(self.iter)
    ####################################################################################

    # Tager og sender indholdet af dit clipboard videre til vores convert to array funktion
    def copyclipboard(self):
        # Pyperclip.paste() tager indholdet af clipboard
        # Kører vores convert to array funktion
        self.converttoarray(str(pyperclip.paste()), 1)

    # Tager og åbner en filedialog til at finde fil, og derefter sender den videre til convert to array funktion
    def openfilearray(self):
        # Skaber de forskellige indstillinger for filedialog
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        # Åbner filedialog med de indstillinger vi vil ha
        filename, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Json Files (*.json);;Text Files (*.txt);;CSV Files (*.csv)", options=options)
        # Åbner og læser den fil der er blevet valgt i filedialog
        file = open(filename, "r")
        filecontent = file.read()
        # Sender indholdet af filen videre til convert to array funktionen
        self.converttoarray(filecontent, 2)
        # Lukker filen igen
        file.close()

    # Funktion til at ændre en string til et array
    def converttoarray(self, userinput, tal):
        # Tager inputtet og replacer alt det vi ikke vil have
        potarray = str(userinput)
        potarray = potarray.replace(" ", "")
        potarray = potarray.replace("[", "")
        potarray = potarray.replace("]", "")
        # Skaber et array ved at splitte ved kommaer
        potarray = potarray.split(",")
        print(potarray)
        # Vi bruger try, for vi har sat det op så det kun virker hvis det er et brugbart array
        try:
            # Bruger int på hver ting i arrayet, sådan at det bliver et tal i stedet for en string
            readyarray = [int(potarray[i]) for i in range(len(potarray))]
            # Sætter self.array til det færdig konverteret array
            self.array = readyarray
            # Ændre vores tekst til en ud af 2 muligheder, alt efter hvad man har valgt
            if tal == 1:
                self.randomizedLabel.setText("Copied From Clipboard")
            elif tal == 2:
                self.randomizedLabel.setText("Copied From File")
            # Denne mulighed burde ikke kunne opnås, men vi har den med som failsafe
            else:
                self.randomizedLabel.setText("What the flip, how did you accomplish this?")
        # Hvis der kommer en error, så er det ikke et rigtigt array
        except:
            self.randomizedLabel.setText("Not A Valid Array")

# Starter vores main-vindue
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

#[5, 3, 2, 1, 7, 4, 8]