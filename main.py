import sys
import os
import random
import pyperclip
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import *
from eksamen.algo.mergesort import Mergesort
from eksamen.algo.bubblesort import Bubblesort
from eksamen.algo.QuickSort import Quicksort

########## Ui til Py ##########
fin = open("gui.ui", 'r')
fout = open("gui.py", 'w')
uic.compileUi(fin, fout, execute=False)
fin.close()
fout.close()
###############################

from eksamen.gui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.array = []
        self.setupUi(self)
        self.fixedRadioFrame.hide()
        self.radioRandom.setChecked(True)
        self.radioRandom.toggled.connect(self.radiohide)
        self.radioFixed.toggled.connect(self.radiohide)
        #Validator til at sørge for man ikke kan lave et random array der er større end 999
        validator1 = QIntValidator(0, 999, self)
        #Validator til at sørge for at neural networks ikke går over 1.000.000 iterations
        validator2 = QIntValidator(0, 1000000, self)
        self.arrayLengthEdit.setValidator(validator1)
        self.neuralLineEdit.setValidator(validator2)
        self.randomizeArrayButton.clicked.connect(self.randomarray)
        self.mergeSortButton.clicked.connect(self.mergesortarray)
        self.bubbleSortButton.clicked.connect(self.bubblesortarray)
        self.copyClipboardButton.clicked.connect(self.copyclipboard)
        self.openFileButton.clicked.connect(self.openfilearray)

    def radiohide(self):
        if self.radioRandom.isChecked():
            self.randomRadioFrame.show()
            self.fixedRadioFrame.hide()
        else:
            self.randomRadioFrame.hide()
            self.fixedRadioFrame.show()

    def randomarray(self):
        if self.arrayLengthEdit.text() != "":
            self.array = [random.randint(1, 1000) for i in range(int(self.arrayLengthEdit.text()))]
            self.randomizedLabel.setText("Randomized")
        else:
            self.randomizedLabel.setText("Insert Number")

    def mergesortarray(self):
        Mergesort(self.array)

    def bubblesortarray(self):
        Bubblesort(self.array)

    def copyclipboard(self):
        self.converttoarray(str(pyperclip.paste()), 1)

    def openfilearray(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Json Files (*.json);;Text Files (*.txt);;CSV Files (*.csv)", options=options)
        file = open(filename, "r")
        filecontent = file.read()
        self.converttoarray(filecontent, 2)
        file.close()

    def converttoarray(self, userinput, tal):
        clipboard = str(userinput)
        clipboard = clipboard.replace(" ", "")
        clipboard = clipboard.replace("[", "")
        clipboard = clipboard.replace("]", "")
        clipboard = clipboard.split(",")
        try:
            cliparray = [int(clipboard[i]) for i in range(len(clipboard))]
            self.array = cliparray
            if tal == 1:
                self.randomizedLabel.setText("Copied From Clipboard")
            elif tal == 2:
                self.randomizedLabel.setText("Copied From File")
            else:
                self.randomizedLabel.setText("What the actual fuck")
        except:
            self.randomizedLabel.setText("Not A Valid Array")

    def exit(self):
        exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

#[5, 3, 2, 1, 7, 4, 8]