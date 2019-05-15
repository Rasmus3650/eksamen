# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(602, 311)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setWindowTitle("Algorithmes")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 601, 291))
        self.tabWidget.setObjectName("tabWidget")
        self.sorting = QtWidgets.QWidget()
        self.sorting.setObjectName("sorting")
        self.radioRandom = QtWidgets.QRadioButton(self.sorting)
        self.radioRandom.setGeometry(QtCore.QRect(180, 21, 111, 21))
        self.radioRandom.setChecked(True)
        self.radioRandom.setObjectName("radioRandom")
        self.fixedRadioFrame = QtWidgets.QFrame(self.sorting)
        self.fixedRadioFrame.setEnabled(True)
        self.fixedRadioFrame.setGeometry(QtCore.QRect(0, 20, 601, 161))
        self.fixedRadioFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fixedRadioFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fixedRadioFrame.setObjectName("fixedRadioFrame")
        self.openFileButton = QtWidgets.QPushButton(self.fixedRadioFrame)
        self.openFileButton.setGeometry(QtCore.QRect(100, 50, 121, 23))
        self.openFileButton.setObjectName("openFileButton")
        self.copyClipboardButton = QtWidgets.QPushButton(self.fixedRadioFrame)
        self.copyClipboardButton.setGeometry(QtCore.QRect(380, 50, 121, 23))
        self.copyClipboardButton.setObjectName("copyClipboardButton")
        self.radioFixed = QtWidgets.QRadioButton(self.sorting)
        self.radioFixed.setGeometry(QtCore.QRect(340, 22, 81, 20))
        self.radioFixed.setObjectName("radioFixed")
        self.randomRadioFrame = QtWidgets.QFrame(self.sorting)
        self.randomRadioFrame.setEnabled(True)
        self.randomRadioFrame.setGeometry(QtCore.QRect(0, 20, 601, 161))
        self.randomRadioFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.randomRadioFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.randomRadioFrame.setObjectName("randomRadioFrame")
        self.arrayLengthEdit = QtWidgets.QLineEdit(self.randomRadioFrame)
        self.arrayLengthEdit.setGeometry(QtCore.QRect(30, 60, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.arrayLengthEdit.setFont(font)
        self.arrayLengthEdit.setObjectName("arrayLengthEdit")
        self.label = QtWidgets.QLabel(self.randomRadioFrame)
        self.label.setGeometry(QtCore.QRect(30, 40, 81, 16))
        self.label.setObjectName("label")
        self.randomizeArrayButton = QtWidgets.QPushButton(self.randomRadioFrame)
        self.randomizeArrayButton.setGeometry(QtCore.QRect(250, 110, 101, 23))
        self.randomizeArrayButton.setObjectName("randomizeArrayButton")
        self.randomizedLabel = QtWidgets.QLabel(self.sorting)
        self.randomizedLabel.setGeometry(QtCore.QRect(0, 160, 601, 21))
        self.randomizedLabel.setText("")
        self.randomizedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.randomizedLabel.setObjectName("randomizedLabel")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.sorting)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 180, 591, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bubbleSortButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.bubbleSortButton.setObjectName("bubbleSortButton")
        self.horizontalLayout_2.addWidget(self.bubbleSortButton)
        self.mergeSortButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.mergeSortButton.setObjectName("mergeSortButton")
        self.horizontalLayout_2.addWidget(self.mergeSortButton)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.fixedRadioFrame.raise_()
        self.randomRadioFrame.raise_()
        self.randomizedLabel.raise_()
        self.radioFixed.raise_()
        self.radioRandom.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.tabWidget.addTab(self.sorting, "Sorting Algorithmes")
        self.neural = QtWidgets.QWidget()
        self.neural.setObjectName("neural")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.neural)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 150, 591, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.neuralButton221 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.neuralButton221.setObjectName("neuralButton221")
        self.horizontalLayout.addWidget(self.neuralButton221)
        self.neuralButton21 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.neuralButton21.setObjectName("neuralButton21")
        self.horizontalLayout.addWidget(self.neuralButton21)
        self.neuralLineEdit = QtWidgets.QLineEdit(self.neural)
        self.neuralLineEdit.setGeometry(QtCore.QRect(30, 70, 531, 31))
        self.neuralLineEdit.setObjectName("neuralLineEdit")
        self.neuralErrorLabel = QtWidgets.QLabel(self.neural)
        self.neuralErrorLabel.setGeometry(QtCore.QRect(30, 120, 531, 20))
        self.neuralErrorLabel.setText("")
        self.neuralErrorLabel.setObjectName("neuralErrorLabel")
        self.label_3 = QtWidgets.QLabel(self.neural)
        self.label_3.setGeometry(QtCore.QRect(30, 50, 71, 16))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.neural, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionRestart = QtWidgets.QAction(MainWindow)
        self.actionRestart.setObjectName("actionRestart")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.radioRandom.setText(_translate("MainWindow", "Random Array"))
        self.openFileButton.setText(_translate("MainWindow", "Open File"))
        self.copyClipboardButton.setText(_translate("MainWindow", "Copy From Clipboard"))
        self.radioFixed.setText(_translate("MainWindow", "Fixed Array"))
        self.label.setText(_translate("MainWindow", "Array Længde:"))
        self.randomizeArrayButton.setText(_translate("MainWindow", "Randomize Array"))
        self.bubbleSortButton.setText(_translate("MainWindow", "Bubblesort"))
        self.mergeSortButton.setText(_translate("MainWindow", "Mergesort"))
        self.pushButton.setText(_translate("MainWindow", "Quicksort"))
        self.neuralButton221.setText(_translate("MainWindow", "Neural Network 2-2-1"))
        self.neuralButton21.setText(_translate("MainWindow", "Neural Network 2-1"))
        self.label_3.setText(_translate("MainWindow", "Iterations:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.neural), _translate("MainWindow", "Neural Network"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionRestart.setText(_translate("MainWindow", "Restart"))

