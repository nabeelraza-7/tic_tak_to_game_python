from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(463, 532)
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        MainWindow.setWindowTitle("Tic Tac Toe|Nabeel Raza, CE-19")
        
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 160, 301, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        
        self.b4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.b4.setFont(font)
        self.b4.setAlignment(QtCore.Qt.AlignCenter)
        self.b4.setObjectName("b4")
        
        self.gridLayout.addWidget(self.b4, 1, 0, 1, 1)
        
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        
        self.b5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.b5.setFont(font)
        self.b5.setAlignment(QtCore.Qt.AlignCenter)
        self.b5.setObjectName("b5")
        
        self.gridLayout.addWidget(self.b5, 1, 1, 1, 1)

        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.b2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.b2.setFont(font)
        self.b2.setAlignment(QtCore.Qt.AlignCenter)
        self.b2.setObjectName("b2")
        
        self.gridLayout.addWidget(self.b2, 0, 1, 1, 1)
        
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        
        self.b7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.b7.setFont(font)
        self.b7.setAlignment(QtCore.Qt.AlignCenter)
        self.b7.setObjectName("b7")
        
        self.gridLayout.addWidget(self.b7, 2, 0, 1, 1)
        
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        
        self.b8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.b8.setFont(font)
        self.b8.setAlignment(QtCore.Qt.AlignCenter)
        self.b8.setObjectName("b8")
        
        self.gridLayout.addWidget(self.b8, 2, 1, 1, 1)
        
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        
        self.b6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.b6.setFont(font)
        self.b6.setAlignment(QtCore.Qt.AlignCenter)
        self.b6.setObjectName("b6")
        
        self.gridLayout.addWidget(self.b6, 1, 2, 1, 1)
        
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        
        self.b3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.b3.setFont(font)
        self.b3.setAlignment(QtCore.Qt.AlignCenter)
        self.b3.setObjectName("b3")
        
        self.gridLayout.addWidget(self.b3, 0, 2, 1, 1)
        
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        
        self.b9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.b9.setFont(font)
        self.b9.setAlignment(QtCore.Qt.AlignCenter)
        self.b9.setObjectName("b9")
        
        self.gridLayout.addWidget(self.b9, 2, 2, 1, 1)
        
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        
        self.b1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.b1.setFont(font)
        self.b1.setAlignment(QtCore.Qt.AlignCenter)
        self.b1.setObjectName("b1")
        
        self.gridLayout.addWidget(self.b1, 0, 0, 1, 1)
        
        self.start = QtWidgets.QPushButton(MainWindow)
        self.start.setGeometry(QtCore.QRect(330,160,75,23))
        self.start.setObjectName("start")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 20, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.score = QtWidgets.QLabel(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(320,370,121,61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        # font.setWeight(75)
        self.score.setFont(font)
        self.score.setText("X:0, O:0")
        self.score.setObjectName("score")
        
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(320, 240, 121, 91))
        self.result.setFont(font)
        self.result.setText("")
        self.result.setObjectName("result")
        
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 111, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.tl = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.tl.setObjectName("tl")
        self.verticalLayout.addWidget(self.tl)
        self.ml = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.ml.setObjectName("ml")
        self.verticalLayout.addWidget(self.ml)
        self.bl = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.bl.setObjectName("bl")
        self.verticalLayout.addWidget(self.bl)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(130, 60, 121, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tm = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.tm.setObjectName("tm")
        self.verticalLayout_2.addWidget(self.tm)
        self.mm = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.mm.setObjectName("mm")
        self.verticalLayout_2.addWidget(self.mm)
        self.bm = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.bm.setObjectName("bm")
        self.verticalLayout_2.addWidget(self.bm)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(260, 60, 121, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tr = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.tr.setObjectName("tr")
        self.verticalLayout_3.addWidget(self.tr)
        self.mr = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.mr.setObjectName("mr")
        self.verticalLayout_3.addWidget(self.mr)
        self.br = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.br.setObjectName("br")
        self.verticalLayout_3.addWidget(self.br)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 463, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.b4.setText(_translate("MainWindow", "_"))
        self.b5.setText(_translate("MainWindow", "_"))
        self.b2.setText(_translate("MainWindow", "_"))
        self.b7.setText(_translate("MainWindow", "_"))
        self.b8.setText(_translate("MainWindow", "_"))
        self.b6.setText(_translate("MainWindow", "_"))
        self.b3.setText(_translate("MainWindow", "_"))
        self.b9.setText(_translate("MainWindow", "_"))
        self.b1.setText(_translate("MainWindow", "_"))
        
        self.start.setText("Restart")
        self.label.setText(_translate("MainWindow", "Tic Tac Toe"))
        self.label_2.setText(_translate("MainWindow", "By Nabeel CE-19"))
        self.score.setText("X:0, O:0")
        self.tl.setText(_translate("MainWindow", "Top-Left"))
        self.ml.setText(_translate("MainWindow", "Mid-Left"))
        self.bl.setText(_translate("MainWindow", "Bottom-Left"))
        self.tm.setText(_translate("MainWindow", "Top-Mid"))
        self.mm.setText(_translate("MainWindow", "Mid-Mid"))
        self.bm.setText(_translate("MainWindow", "Bottom-Mid"))
        self.tr.setText(_translate("MainWindow", "Top-Right"))
        self.mr.setText(_translate("MainWindow", "Mid-Right"))
        self.br.setText(_translate("MainWindow", "Bottom-Right"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())