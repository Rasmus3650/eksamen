from PyQt4 import uic
import sys
from PyQt4.QtGui import *

def konverter():
    if (len(indfil.text()) == 0):
        fin = open("C:/Users/2112r/PycharmProjects/Eksamen_lodtrækning/Lodtrækning_ui.ui", 'r')
        fout = open("C:/Users/2112r/PycharmProjects/Eksamen_lodtrækning/Lodtrækning_py.py", 'w')
        uic.compileUi(fin, fout, execute=False)
        fin.close()
        fout.close()
    else:
        fin = open(indfil.text(),'r')
        fout = open(udfil.text(),'w')
        uic.compileUi(fin,fout,execute=False)
        fin.close()
        fout.close()


# Opretter QT4 app objekt
a = QApplication(sys.argv)

# QWidget widget er grundklassen for alle brugergrænseflade-objekter i PyQt4.
w = QWidget()

# Viduets størrelse.
w.resize(320, 240)

# Viduets Titel
w.setWindowTitle("Ui til Py")

indlabel = QLabel('Sti til ui filen',w)
indfil = QLineEdit(w)
indfil.move(0,20)
indfil.resize(300,20)

udlabel = QLabel('Navn til py filen',w)
udfil = QLineEdit(w)
udfil.move(0,100)
udfil.resize(300,20)
udlabel.move(0,80)

knap = QPushButton('Konverter!',w)
knap.move(0,140)
knap.clicked.connect(konverter)


# Viser vinduet
w.show()

sys.exit(a.exec_())
