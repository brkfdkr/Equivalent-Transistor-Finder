from PyQt5 import QtCore, QtGui, QtWidgets


class scrmain(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(610, 600)
        self.label_LutfenTransistorDegerleriniGiriniz = QtWidgets.QLabel(Form)
        self.label_LutfenTransistorDegerleriniGiriniz.setGeometry(QtCore.QRect(10, 10, 311, 41))
        self.label_LutfenTransistorDegerleriniGiriniz.setFrameShape(QtWidgets.QFrame.Box)
        self.label_LutfenTransistorDegerleriniGiriniz.setLineWidth(2)
        self.label_LutfenTransistorDegerleriniGiriniz.setMidLineWidth(1)
        self.label_LutfenTransistorDegerleriniGiriniz.setObjectName("label_LutfenTransistorDegerleriniGiriniz")
        self.line_ = QtWidgets.QFrame(Form)
        self.line_.setGeometry(QtCore.QRect(350, 20, 20, 550))
        self.line_.setMidLineWidth(3)
        self.line_.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_.setObjectName("line_")
        self.label_MuadilTransistorListesi = QtWidgets.QLabel(Form)
        self.label_MuadilTransistorListesi.setGeometry(QtCore.QRect(390, 10, 191, 41))
        self.label_MuadilTransistorListesi.setFrameShape(QtWidgets.QFrame.Box)
        self.label_MuadilTransistorListesi.setLineWidth(2)
        self.label_MuadilTransistorListesi.setMidLineWidth(1)
        self.label_MuadilTransistorListesi.setObjectName("label_MuadilTransistorListesi")
        self.label_TransistorTipi = QtWidgets.QLabel(Form)
        self.label_TransistorTipi.setGeometry(QtCore.QRect(10, 60, 75, 13))
        self.label_TransistorTipi.setObjectName("label_TransistorTipi")
        self.label_Pgm = QtWidgets.QLabel(Form)
        self.label_Pgm.setGeometry(QtCore.QRect(90, 90, 47, 16))
        self.label_Pgm.setObjectName("label_Pgm")
        self.lineEdit_Pgm1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_Pgm1.setGeometry(QtCore.QRect(10, 90, 61, 20))
        self.lineEdit_Pgm1.setObjectName("lineEdit_Pgm1")
        self.lineEdit_Pgm2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_Pgm2.setGeometry(QtCore.QRect(160, 90, 61, 20))
        self.lineEdit_Pgm2.setObjectName("lineEdit_Pgm2")
        self.label_Watt = QtWidgets.QLabel(Form)
        self.label_Watt.setGeometry(QtCore.QRect(230, 90, 47, 13))
        self.label_Watt.setObjectName("label_Watt")
        self.lineEdit_Vdrm1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_Vdrm1.setGeometry(QtCore.QRect(10, 120, 61, 20))
        self.lineEdit_Vdrm1.setObjectName("lineEdit_Vdrm1")
        self.lineEdit_Vdrm2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_Vdrm2.setGeometry(QtCore.QRect(160, 120, 61, 20))
        self.lineEdit_Vdrm2.setObjectName("lineEdit_Vdrm2")
        self.lineEdit_Itavr1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_Itavr1.setGeometry(QtCore.QRect(10, 150, 61, 20))
        self.lineEdit_Itavr1.setObjectName("lineEdit_Itavr1")
        self.lineEdit_Itavr2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_Itavr2.setGeometry(QtCore.QRect(160, 150, 61, 20))
        self.lineEdit_Itavr2.setObjectName("lineEdit_Itavr2")
        self.lineEdit_Itrms1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_Itrms1.setGeometry(QtCore.QRect(10, 180, 61, 20))
        self.lineEdit_Itrms1.setObjectName("lineEdit_Itrms1")
        self.lineEdit_Itrms2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_Itrms2.setGeometry(QtCore.QRect(160, 180, 61, 20))
        self.lineEdit_Itrms2.setObjectName("lineEdit_Itrms2")
        self.lineEdit_Itsm1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_Itsm1.setGeometry(QtCore.QRect(10, 210, 61, 20))
        self.lineEdit_Itsm1.setObjectName("lineEdit_Itsm1")
        self.lineEdit_Itsm2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_Itsm2.setGeometry(QtCore.QRect(160, 210, 61, 20))
        self.lineEdit_Itsm2.setObjectName("lineEdit_Itsm2")
        self.lineEdit_dldt1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_dldt1.setGeometry(QtCore.QRect(10, 240, 61, 20))
        self.lineEdit_dldt1.setObjectName("lineEdit_dldt1")
        self.lineEdit_dldt2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_dldt2.setGeometry(QtCore.QRect(160, 240, 61, 20))
        self.lineEdit_dldt2.setObjectName("lineEdit_dldt2")
        self.lineEdit_dVdt1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_dVdt1.setGeometry(QtCore.QRect(10, 270, 61, 20))
        self.lineEdit_dVdt1.setObjectName("lineEdit_dVdt1")
        self.lineEdit_dVdt2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_dVdt2.setGeometry(QtCore.QRect(160, 270, 61, 20))
        self.lineEdit_dVdt2.setObjectName("lineEdit_dVdt2")
        self.lineEdit_TstgTj = QtWidgets.QLineEdit(Form)
        self.lineEdit_TstgTj.setGeometry(QtCore.QRect(90, 300, 61, 20))
        self.lineEdit_TstgTj.setObjectName("lineEdit_TstgTj")
        self.lineEdit_Rthja = QtWidgets.QLineEdit(Form)
        self.lineEdit_Rthja.setGeometry(QtCore.QRect(90, 330, 61, 20))
        self.lineEdit_Rthja.setObjectName("lineEdit_Rthja")
        self.lineEdit_Rthjc = QtWidgets.QLineEdit(Form)
        self.lineEdit_Rthjc.setGeometry(QtCore.QRect(90, 360, 61, 20))
        self.lineEdit_Rthjc.setObjectName("lineEdit_Rthjc")
        
        self.lineEdit_Vgt = QtWidgets.QLineEdit(Form)
        self.lineEdit_Vgt.setGeometry(QtCore.QRect(90, 390, 61, 20))
        self.lineEdit_Vgt.setObjectName("lineEdit_Vgt")
        self.label_Vdrm = QtWidgets.QLabel(Form)
        self.label_Vdrm.setGeometry(QtCore.QRect(90, 120, 50, 16))
        self.label_Vdrm.setObjectName("label_Vdrm")
        self.lineEdit_Vtm = QtWidgets.QLineEdit(Form)
        self.lineEdit_Vtm.setGeometry(QtCore.QRect(90, 420, 61, 20))
        self.lineEdit_Vtm.setObjectName("lineEdit_Vtm")
        self.lineEdit_Igt = QtWidgets.QLineEdit(Form)
        self.lineEdit_Igt.setGeometry(QtCore.QRect(90, 450, 61, 20))
        self.lineEdit_Igt.setObjectName("lineEdit_Igt")
        self.lineEdit_Ih = QtWidgets.QLineEdit(Form)
        self.lineEdit_Ih.setGeometry(QtCore.QRect(90, 480, 61, 20))
        self.lineEdit_Ih.setObjectName("lineEdit_Ih")
        self.lineEdit_Paketturu = QtWidgets.QLineEdit(Form)
        self.lineEdit_Paketturu.setGeometry(QtCore.QRect(90, 510, 61, 20))
        self.lineEdit_Paketturu.setObjectName("lineEdit_Paketturu")
        self.label_Itavr = QtWidgets.QLabel(Form)
        self.label_Itavr.setGeometry(QtCore.QRect(90, 150, 55, 16))
        self.label_Itavr.setObjectName("label_Itavr")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 180, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_Itsm = QtWidgets.QLabel(Form)
        self.label_Itsm.setGeometry(QtCore.QRect(90, 210, 60, 16))
        self.label_Itsm.setObjectName("label_Itsm")
        self.label_dldt = QtWidgets.QLabel(Form)
        self.label_dldt.setGeometry(QtCore.QRect(90, 240, 60, 16))
        self.label_dldt.setObjectName("label_dldt")
        self.label_dVdt = QtWidgets.QLabel(Form)
        self.label_dVdt.setGeometry(QtCore.QRect(90, 270, 60, 16))
        self.label_dVdt.setObjectName("label_dVdt")
        self.label_Volt = QtWidgets.QLabel(Form)
        self.label_Volt.setGeometry(QtCore.QRect(230, 120, 47, 13))
        self.label_Volt.setObjectName("label_Volt")
        self.label_Amper1 = QtWidgets.QLabel(Form)
        self.label_Amper1.setGeometry(QtCore.QRect(230, 150, 47, 13))
        self.label_Amper1.setObjectName("label_Amper1")
        self.label_Amper2 = QtWidgets.QLabel(Form)
        self.label_Amper2.setGeometry(QtCore.QRect(230, 180, 47, 13))
        self.label_Amper2.setObjectName("label_Amper2")
        self.label_Amper3 = QtWidgets.QLabel(Form)
        self.label_Amper3.setGeometry(QtCore.QRect(230, 210, 47, 13))
        self.label_Amper3.setObjectName("label_Amper3")
        self.label_Ampermikrosaniye = QtWidgets.QLabel(Form)
        self.label_Ampermikrosaniye.setGeometry(QtCore.QRect(230, 240, 125, 13))
        self.label_Ampermikrosaniye.setObjectName("label_Ampermikrosaniye")
        self.label_Voltmikrosaniye = QtWidgets.QLabel(Form)
        self.label_Voltmikrosaniye.setGeometry(QtCore.QRect(230, 270, 125, 13))
        self.label_Voltmikrosaniye.setObjectName("label_Voltmikrosaniye")
        self.label_Adet = QtWidgets.QLabel(Form)
        self.label_Adet.setGeometry(QtCore.QRect(370, 450, 141, 21))
        self.label_Adet.setObjectName("label_Adet")
        self.btn_yardim = QtWidgets.QPushButton(Form)
        self.btn_yardim.setGeometry(QtCore.QRect(510, 550, 75, 23))
        self.btn_yardim.setObjectName("btn_yardim")
        self.label_TstgTj = QtWidgets.QLabel(Form)
        self.label_TstgTj.setGeometry(QtCore.QRect(30, 300, 47, 16))
        self.label_TstgTj.setObjectName("label_TstgTj")
        self.label_Rthja = QtWidgets.QLabel(Form)
        self.label_Rthja.setGeometry(QtCore.QRect(30, 330, 47, 16))
        self.label_Rthja.setObjectName("label_Rthja")
        self.label_Rthjc = QtWidgets.QLabel(Form)
        self.label_Rthjc.setGeometry(QtCore.QRect(30, 360, 47, 16))
        self.label_Rthjc.setObjectName("label_Rthjc")
        self.label_Vgt = QtWidgets.QLabel(Form)
        self.label_Vgt.setGeometry(QtCore.QRect(30, 390, 47, 16))
        self.label_Vgt.setObjectName("label_Vgt")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(30, 420, 47, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(30, 450, 47, 16))
        self.label_9.setObjectName("label_9")
        self.label_Ih = QtWidgets.QLabel(Form)
        self.label_Ih.setGeometry(QtCore.QRect(30, 480, 47, 16))
        self.label_Ih.setObjectName("label_Ih")
        self.label_Celsius = QtWidgets.QLabel(Form)
        self.label_Celsius.setGeometry(QtCore.QRect(170, 300, 47, 13))
        self.label_Celsius.setObjectName("label_Celsius")
        self.label_KelvinWatt1 = QtWidgets.QLabel(Form)
        self.label_KelvinWatt1.setGeometry(QtCore.QRect(170, 330, 90, 13))
        self.label_KelvinWatt1.setObjectName("label_KelvinWatt1")
        self.label_KelvinWatt2 = QtWidgets.QLabel(Form)
        self.label_KelvinWatt2.setGeometry(QtCore.QRect(170, 360, 90, 13))
        self.label_KelvinWatt2.setObjectName("label_KelvinWatt2")
        self.label_Volt1 = QtWidgets.QLabel(Form)
        self.label_Volt1.setGeometry(QtCore.QRect(170, 390, 47, 13))
        self.label_Volt1.setObjectName("label_Volt1")
        self.label_Volt2 = QtWidgets.QLabel(Form)
        self.label_Volt2.setGeometry(QtCore.QRect(170, 420, 47, 13))
        self.label_Volt2.setObjectName("label_Volt2")
        self.label_Miliamper1 = QtWidgets.QLabel(Form)
        self.label_Miliamper1.setGeometry(QtCore.QRect(170, 450, 75, 13))
        self.label_Miliamper1.setObjectName("label_Miliamper1")
        self.label_Miliamper2 = QtWidgets.QLabel(Form)
        self.label_Miliamper2.setGeometry(QtCore.QRect(170, 480, 75, 13))
        self.label_Miliamper2.setObjectName("label_Miliamper2")
        self.label_Paketturu = QtWidgets.QLabel(Form)
        self.label_Paketturu.setGeometry(QtCore.QRect(20, 510, 85, 16))
        self.label_Paketturu.setObjectName("label_Paketturu")
        self.btn_ara = QtWidgets.QPushButton(Form)
        self.btn_ara.setGeometry(QtCore.QRect(40, 550, 75, 23))
        self.btn_ara.setObjectName("btn_ara")
        self.btn_temizle = QtWidgets.QPushButton(Form)
        self.btn_temizle.setGeometry(QtCore.QRect(130, 550, 75, 23))
        self.btn_temizle.setObjectName("btn_temizle")
        self.btn_geri = QtWidgets.QPushButton(Form)
        self.btn_geri.setGeometry(QtCore.QRect(220, 550, 75, 23))
        self.btn_geri.setObjectName("btn_geri")
        self.box_type1 = QtWidgets.QComboBox(Form)
        self.box_type1.setGeometry(QtCore.QRect(90, 60, 120, 22))
        self.box_type1.setObjectName("box_type1")
        self.box_type1.addItem("")
        self.box_type1.addItem("")
        self.box_type1.addItem("")
        self.liste4 = QtWidgets.QListWidget(Form)
        self.liste4.setGeometry(QtCore.QRect(370, 60, 231, 381))
        self.liste4.setObjectName("liste4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Muadil Transistör Bulucu"))
        self.label_LutfenTransistorDegerleriniGiriniz.setText(_translate("Form", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; font-weight:600; font-style:italic;\">Lütfen Transistör Değerlerini Giriniz</span></p></body></html>"))
        self.label_MuadilTransistorListesi.setText(_translate("Form", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; font-weight:600; font-style:italic;\">Muadil Transistör Listesi</span></p></body></html>"))
        self.label_TransistorTipi.setText(_translate("Form", "Transistör Tipi:"))
        self.label_Pgm.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">&lt; </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff;\">P</span><span style=\" font-size:9pt; font-weight:600; color:#000000; vertical-align:sub;\">GM </span><span style=\" font-size:9pt; font-weight:600;\">&lt;</span></p></body></html>"))
        self.label_Watt.setText(_translate("Form", "W(Watt)"))
        self.label_Vdrm.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">&lt;</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff;\"> V</span><span style=\" font-size:9pt; font-weight:600; vertical-align:sub;\">DRM </span><span style=\" font-size:9pt; font-weight:600;\">&lt;</span></p></body></html>"))
        self.label_Itavr.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">&lt; </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff;\">I</span><span style=\" font-size:9pt; font-weight:600; vertical-align:sub;\">T(AVR</span><span style=\" font-weight:600; vertical-align:sub;\">) </span><span style=\" font-size:9pt; font-weight:600;\">&lt;</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">&lt;</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff;\"> I</span><span style=\" font-size:9pt; font-weight:600; vertical-align:sub;\">T(RMS) </span><span style=\" font-size:9pt; font-weight:600;\">&lt;</span></p></body></html>"))
        self.label_Itsm.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">&lt; </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff;\">I</span><span style=\" font-size:9pt; font-weight:600; vertical-align:sub;\">TSM</span><span style=\" font-size:9pt; font-weight:600;\"> &lt;</span></p></body></html>"))
        self.label_dldt.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">&lt;</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff;\"> dI/dt </span><span style=\" font-size:9pt; font-weight:600;\">&lt;</span></p></body></html>"))
        self.label_dVdt.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">&lt;</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff;\"> dV/dt </span><span style=\" font-size:9pt; font-weight:600;\">&lt;</span></p></body></html>"))
        self.label_Volt.setText(_translate("Form", "V(Volt)"))
        self.label_Amper1.setText(_translate("Form", "A(Amper)"))
        self.label_Amper2.setText(_translate("Form", "A(Amper)"))
        self.label_Amper3.setText(_translate("Form", "A(Amper)"))
        self.label_Ampermikrosaniye.setText(_translate("Form", "A/µs(Amper/Mikrosaniye)"))
        self.label_Voltmikrosaniye.setText(_translate("Form", "V/µs(Volt/Mikrosaniye)"))
        self.label_Adet.setText(_translate("Form", "Adet:"))
        self.btn_yardim.setText(_translate("Form", "Yardım"))
        self.label_TstgTj.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff;\">T</span><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff; vertical-align:sub;\">stg</span><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff;\">, T</span><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff; vertical-align:sub;\">j </span><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff;\">&gt;</span></p></body></html>"))
        self.label_Rthja.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff;\">R</span><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff; vertical-align:sub;\">TH(j-a) </span><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff;\">&lt;</span></p></body></html>"))
        self.label_Rthjc.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff;\">R</span><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff; vertical-align:sub;\">TH(j-c) </span><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff;\">&lt;</span></p></body></html>"))
        self.label_Vgt.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff;\">V</span><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff; vertical-align:sub;\">GT </span><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff;\">&lt;</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff;\">V</span><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff; vertical-align:sub;\">TM </span><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff;\">&lt;</span></p></body></html>"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff;\">I</span><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff; vertical-align:sub;\">GT </span><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff;\">&lt;</span></p></body></html>"))
        self.label_Ih.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff;\">I</span><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff; vertical-align:sub;\">H </span><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:#ffffff;\">&lt;</span></p></body></html>"))
        self.label_Celsius.setText(_translate("Form", "C(Celsius)"))
        self.label_KelvinWatt1.setText(_translate("Form", "K/W(Kelvin/Watt)"))
        self.label_KelvinWatt2.setText(_translate("Form", "K/W(Kelvin/Watt)"))
        self.label_Volt1.setText(_translate("Form", "V(Volt)"))
        self.label_Volt2.setText(_translate("Form", "V(Volt)"))
        self.label_Miliamper1.setText(_translate("Form", "mA(Miliamper)"))
        self.label_Miliamper2.setText(_translate("Form", "mA(Miliamper)"))
        self.label_Paketturu.setText(_translate("Form", "<html><head/><body><p>Paket Türü:</p></body></html>"))
        self.btn_ara.setText(_translate("Form", "Ara"))
        self.btn_temizle.setText(_translate("Form", "Temizle"))
        self.btn_geri.setText(_translate("Form", "Geri"))
        self.box_type1.setItemText(0, _translate("Form", "SCR"))
        self.box_type1.setItemText(1, _translate("Form", "SCR-module"))
        self.box_type1.setItemText(2, _translate("Form", "Triac"))


