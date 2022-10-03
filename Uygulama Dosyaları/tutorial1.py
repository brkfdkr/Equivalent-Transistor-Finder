# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tutorial122.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class tutorial(object):
    def setupUi(self, tutorial):
        tutorial.setObjectName("tutorial")
        tutorial.resize(751, 633)
        self.centralwidget = QtWidgets.QWidget(tutorial)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 421, 401))
        self.label.setObjectName("label")
        self.btn_geri = QtWidgets.QPushButton(self.centralwidget)
        self.btn_geri.setGeometry(QtCore.QRect(10, 550, 75, 23))
        self.btn_geri.setObjectName("btn_geri")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 380, 561, 151))
        self.label_2.setObjectName("label_2")
        tutorial.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(tutorial)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 21))
        self.menubar.setObjectName("menubar")
        tutorial.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(tutorial)
        self.statusbar.setObjectName("statusbar")
        tutorial.setStatusBar(self.statusbar)

        self.retranslateUi(tutorial)
        QtCore.QMetaObject.connectSlotsByName(tutorial)

    def retranslateUi(self, tutorial):
        _translate = QtCore.QCoreApplication.translate
        tutorial.setWindowTitle(_translate("tutorial", "Muadil Transistör Bulucu"))
        self.label.setText(_translate("tutorial", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">BJT için Transistör Değerleri:</span></p><p>Transistör Materyali (Si)</p><p>Polarity (NPN) = Polarite/Kutupluk </p><p>Maximum Collector Power Dissipation (Pc) = Maksimum Dayanma Gücü</p><p>Maximum Collector-Base Voltage (Vcb) = Maksimum Kollektör Beyz Gerilimi</p><p>Maximum Collector-Emitter Voltage (Vce) = Maksimum Kollektör-Emiter Gerilimi</p><p>Maximum Emitter-Base Voltage (Veb) = Maksimum Emiter-Beyz Gerilimi</p><p>Maximum Collector Current (Ic max) = Maksimum Kollektör Akımı</p><p>Max. Operating Junction Temperature (Tj) = Maksimum Jonksiyon Sıcaklığı</p><p>Transition Frequency (ft) = Maksimum Çalışma Frekansı</p><p>Collector Capacitance (Cc) = Kollektör Kapansitansı</p><p>Forward Current Transfer Ratio (hFE), MIN:100 = Akım Kazancı</p><p>Noise Figure, dB = Gürültü Sayısı</p><p>Package(ör: TO3P,TO220AB,MODULE) = Paket Türü</p><p><br/></p></body></html>"))
        self.btn_geri.setText(_translate("tutorial", "Geri"))
        self.label_2.setText(_translate("tutorial", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Butonlar:</span></p><p><span style=\" text-decoration: underline;\">Ara</span>: Girilen değerlere göre muadil transistörleri bulur.</p><p><span style=\" text-decoration: underline;\">Temizle:</span> Daha önceden arama yapılmışsa listeyi ve girilen değerleri temizler.</p><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#343434;\">Sayfa Sayısı:</span></p><p><span style=\" color:#343434;\">Her sayfada en fazla 1000 değer gözükmektedir. Bu nedenle aradığınız transistör yoksa &quot;Sayfa: &quot;</span></p><p><span style=\" color:#343434;\"> bölmesine istediğiniz sayfanın numarasını giriniz ve &quot;Ara&quot; butonuna basınız. </span></p></body></html>"))

