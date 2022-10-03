# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tutorialigbt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class tutorial2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(609, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 461, 331))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 310, 551, 211))
        self.label_2.setObjectName("label_2")
        self.btn_geri = QtWidgets.QPushButton(self.centralwidget)
        self.btn_geri.setGeometry(QtCore.QRect(20, 510, 75, 23))
        self.btn_geri.setObjectName("btn_geri")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 609, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">IGBT İçin Transistör Değerleri:</span></p><p><br/></p><p>Struct(N,P) = Yapı</p><p>Maximum Power Capacity (P<span style=\" vertical-align:sub;\">C</span>) = Maksimum Güç Kapasitesi</p><p>Collector-Emitter Voltage (V<span style=\" vertical-align:sub;\">CE</span>) = Kollektör-Emiter Gerilimi</p><p>Collector-Emitter Saturation Voltage (V<span style=\" vertical-align:sub;\">CE</span>) = Kollektör-Emiter Doyma Gerilimi</p><p>Gate-Emitter Voltage (V<span style=\" vertical-align:sub;\">EG</span>) = Gate-Emiter Gerilimi</p><p>Continuous Collector Current (I<span style=\" vertical-align:sub;\">C</span>) = Sürekli Kollektör Akımı</p><p>Maximum Junction Temperature (T<span style=\" vertical-align:sub;\">J</span>) = Maksimum Jonksiyon Sıcaklığı</p><p>Rise Time (t<span style=\" vertical-align:sub;\">r</span>) = Yükselme Zamanı</p><p>Maximum Collector Capacity (C<span style=\" vertical-align:sub;\">C</span>) = Maksimum Kollektör Kapasitansı</p><p>Package(ör: TO3P,MODULE,KT9M,...) = Paket Türü</p><p><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><br/><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Butonlar:</span></p><p><span style=\" font-size:10pt; text-decoration: underline;\">Ara:</span><span style=\" font-size:10pt;\"> Girilen değere göre muadil transistörleri bulur.</span></p><p><span style=\" font-size:10pt; text-decoration: underline;\">Temizle:</span><span style=\" font-size:10pt;\"> Daha önceden arama yapılmışsa listeyi ve girilen değerleri temizler.</span></p><p><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Sayfa Sayısı :</span></p><p><span style=\" font-size:10pt;\">En fazla 1000 adet IGBT değeri gösterilmektedir bu nedenle bu bölümde sayfa sayısı yoktur.</span></p></body></html>"))
        self.btn_geri.setText(_translate("MainWindow", "Geri"))


