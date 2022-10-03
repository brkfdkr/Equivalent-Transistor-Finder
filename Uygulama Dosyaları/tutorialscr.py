# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tutorialscr.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class tutorial4(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 635)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 380, 551, 211))
        self.label_2.setObjectName("label_2")
        self.btn_geri = QtWidgets.QPushButton(self.centralwidget)
        self.btn_geri.setGeometry(QtCore.QRect(20, 560, 75, 23))
        self.btn_geri.setObjectName("btn_geri")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 521, 471))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
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
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><br/><span style=\" font-weight:600; font-style:italic;\">Butonlar:</span></p><p><span style=\" text-decoration: underline;\">Ara:</span> Girilen değere göre muadil transistörleri bulur.</p><p><span style=\" text-decoration: underline;\">Temizle:</span> Daha önceden arama yapılmışsa listeyi ve girilen değerleri temizler.</p><p><span style=\" font-weight:600; font-style:italic;\">Sayfa Sayısı :</span></p><p>En fazla 1000 adet SCR değeri gösterilmektedir bu nedenle bu bölümde sayfa sayısı yoktur.</p></body></html>"))
        self.btn_geri.setText(_translate("MainWindow", "Geri"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">SCR İçin Transistör Değerleri</span></p><p>Type = Tür (SCR, SCR-module ya da Triac)</p><p>Maximum Peak Gate Power (P<span style=\" vertical-align:sub;\">GM</span>) = Maksimum Tepe Gate Gücü</p><p>Peak Repetitive Off−State Voltage (V<span style=\" vertical-align:sub;\">DRM</span>) = Tekrarlayan İletken Olmayan Durum Tepe Gerilimi</p><p>Average on-state current (I<span style=\" vertical-align:sub;\">T(AVR)</span>) = Ortalama İletken Durum Akımı</p><p>On-State RMS (root mean square) Current (I<span style=\" vertical-align:sub;\">T(RMS)</span>) = İletken Durum RMS Akımı</p><p>Non Repetitive Surge Peak On-State Current (I<span style=\" vertical-align:sub;\">TSM</span>) = Tekrarsız İletken Tepe Dalgalanma Akımı</p><p>Critical repetitive rate of rise of on-state current (d<span style=\" vertical-align:sub;\">I</span>/d<span style=\" vertical-align:sub;\">t</span>) = İletken Akımdaki Kritik Tekrarlayan Yükselme Oranı</p><p>Critical rate of rise of off-state voltage (d<span style=\" vertical-align:sub;\">V</span>/d<span style=\" vertical-align:sub;\">t</span>) = İlekten Olmayan Durum Gerilimdeki Kritik Yükselme Oranı</p><p>Storage and Operating Junction Temperatures (T<span style=\" vertical-align:sub;\">stg</span>, T<span style=\" vertical-align:sub;\">j</span>) = Depolama ve Jonksiyon Sıcaklıkları</p><p>Junction to ambient thermal resistance (R<span style=\" vertical-align:sub;\">TH(j-a)</span>) = Jonksiyon – Çevre Isıl Direnci</p><p>Junction to case thermal resistance (R<span style=\" vertical-align:sub;\">TH(j-c)</span>) = Jonksiyon – Kılıf Isıl Direnci</p><p>Triggering gate voltage (V<span style=\" vertical-align:sub;\">GT</span>) = Tetikleyen Gate Gerilimi</p><p>Peak On-State Voltage Drop (V<span style=\" vertical-align:sub;\">TM</span>) = Tepe İletken Durumunda Düşme Gerilimi</p><p>Triggering Gate Current (I<span style=\" vertical-align:sub;\">GT</span>) = Tetikleyen Gate Akımı</p><p>Holding Current (I<span style=\" vertical-align:sub;\">H</span>) = Tutma Akımı</p><p>Package(ör: TO208AB,TO9,TO18,...) = Paket Türü</p><p><br/></p></body></html>"))


