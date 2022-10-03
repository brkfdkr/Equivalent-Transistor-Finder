# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tutorialmosfet.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class tutorial3(object):
    def setupUi(self, tutorialmosfet):
        tutorialmosfet.setObjectName("tutorialmosfet")
        tutorialmosfet.resize(615, 639)
        self.centralwidget = QtWidgets.QWidget(tutorialmosfet)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, -10, 511, 471))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 360, 601, 211))
        self.label_2.setObjectName("label_2")
        self.btn_geri = QtWidgets.QPushButton(self.centralwidget)
        self.btn_geri.setGeometry(QtCore.QRect(20, 550, 75, 23))
        self.btn_geri.setObjectName("btn_geri")
        tutorialmosfet.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(tutorialmosfet)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 21))
        self.menubar.setObjectName("menubar")
        tutorialmosfet.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(tutorialmosfet)
        self.statusbar.setObjectName("statusbar")
        tutorialmosfet.setStatusBar(self.statusbar)

        self.retranslateUi(tutorialmosfet)
        QtCore.QMetaObject.connectSlotsByName(tutorialmosfet)

    def retranslateUi(self, tutorialmosfet):
        _translate = QtCore.QCoreApplication.translate
        tutorialmosfet.setWindowTitle(_translate("tutorialmosfet", "MainWindow"))
        self.label.setText(_translate("tutorialmosfet", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">MOSFET/JFET İçin Transistör Değerleri:</span></p><p><br/></p><p>Struct(MOSFET veya JFET) = Yapı</p><p>Polarity (N,P,...) = Polarite/Kutupluk </p><p>Maximum Power Dissipation (P<span style=\" vertical-align:sub;\">D</span>) = Maksimum Güç Dağılımı</p><p>Drain-Source Breakdown Voltage (V<span style=\" vertical-align:sub;\">DS</span>) = Drain-Source Kırılma Gerilimi</p><p>Gate-Source Voltage (V<span style=\" vertical-align:sub;\">GS</span>) = Gate-Source Gerilimi</p><p>Gate Threshold Voltage V<span style=\" vertical-align:sub;\">GS</span>(th) = Gate Threshold Gerilimi</p><p>Maximum Drain Current (I<span style=\" vertical-align:sub;\">d</span>) = Maksimum Drain Akımı</p><p>Maximum Junction Temperature (T<span style=\" vertical-align:sub;\">J</span>) = Maksimum Jonksiyon Sıcaklığı</p><p>Total Gate Charge (Q<span style=\" vertical-align:sub;\">G</span>) = Toplam Gate Yükü</p><p>Rise Time (t<span style=\" vertical-align:sub;\">r</span>) = Yükselme Zamanı</p><p>Drain-Source Capacitance (C<span style=\" vertical-align:sub;\">D</span>) = Drain-Source Kapasitansı</p><p>Maximum Drain-Source On-State Resistance (R<span style=\" vertical-align:sub;\">DS</span>) = Maksimum Drain-Source Direnci</p><p>Package(ör: TO92,TO220F,SOT92,...) = Paket Türü</p><p><br/></p></body></html>"))
        self.label_2.setText(_translate("tutorialmosfet", "<html><head/><body><p><br/><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Butonlar:</span></p><p><span style=\" font-size:10pt; text-decoration: underline;\">Ara:</span><span style=\" font-size:10pt;\"> Girilen değere göre muadil transistörleri bulur.</span></p><p><span style=\" font-size:10pt; text-decoration: underline;\">Temizle:</span><span style=\" font-size:10pt;\"> Daha önceden arama yapılmışsa listeyi ve girilen değerleri temizler.</span></p><p><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Sayfa Sayısı :</span></p><p><span style=\" font-size:10pt;\">En fazla 1000 adet MOSFET-JFET değeri gösterilmektedir bu nedenle bu bölümde sayfa sayısı yoktur.</span></p></body></html>"))
        self.btn_geri.setText(_translate("tutorialmosfet", "Geri"))


