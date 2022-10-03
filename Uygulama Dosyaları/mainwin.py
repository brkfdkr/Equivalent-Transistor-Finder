# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.setWindowModality(QtCore.Qt.WindowModal)
        main.resize(575, 606)
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 271, 61))
        self.label.setObjectName("label")
        self.btn_bjt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bjt.setGeometry(QtCore.QRect(30, 60, 241, 51))
        self.btn_bjt.setObjectName("btn_bjt")
        self.btn_mosfet = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mosfet.setGeometry(QtCore.QRect(30, 130, 241, 51))
        self.btn_mosfet.setObjectName("btn_mosfet")
        self.btn_igbt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_igbt.setGeometry(QtCore.QRect(30, 200, 241, 51))
        self.btn_igbt.setObjectName("btn_igbt")
        self.btn_scr = QtWidgets.QPushButton(self.centralwidget)
        self.btn_scr.setGeometry(QtCore.QRect(30, 270, 241, 51))
        self.btn_scr.setObjectName("btn_scr")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(232, 30, 111, 541))
        self.line.setMidLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 50, 191, 271))
        self.label_2.setObjectName("label_2")
        main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 575, 21))
        self.menubar.setObjectName("menubar")
        main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main)
        self.statusbar.setObjectName("statusbar")
        main.setStatusBar(self.statusbar)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Muadil Transistör Bulucu"))
        self.label.setText(_translate("main", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Lütfen Transistör Türünü Seçiniz</span></p></body></html>"))
        self.btn_bjt.setText(_translate("main", "BJT"))
        self.btn_mosfet.setText(_translate("main", "MOSFET-JFET"))
        self.btn_igbt.setText(_translate("main", "IGBT"))
        self.btn_scr.setText(_translate("main", "SCR"))
        self.label_2.setText(_translate("main", "<html><head/><body><p><img src=\":/İtü/itu-istanbul-teknik_universitesi-logo.png\"/></p></body></html>"))
import Resim


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())
