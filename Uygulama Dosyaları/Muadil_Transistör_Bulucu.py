from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup

from mainwin import Ui_main
from bjt_main import bjtmain
from igbt_main import igbtmain
from mosfet_main import mosfetmain
from scr_main import scrmain
from tutorial1 import tutorial
from tutorialigbt import tutorial2
from tutorialmosfet import tutorial3
from tutorialscr import tutorial4

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

import sys

#Ana Menünün classı
class mainwdw(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainwdw,self).__init__()
        self.ui = Ui_main()
        self.ui.setupUi(self)
        self.ui.btn_bjt.clicked.connect(self.gobjt)
        self.ui.btn_igbt.clicked.connect(self.goigbt)
        self.ui.btn_mosfet.clicked.connect(self.gomosfet)
        self.ui.btn_scr.clicked.connect(self.goscr)

    def gobjt(self):
        mainn.setCurrentIndex(mainn.currentIndex()+1)
    def goigbt(self):
        mainn.setCurrentIndex(mainn.currentIndex()+3)
    def gomosfet(self):
        mainn.setCurrentIndex(mainn.currentIndex()+5)
    def goscr(self):
        mainn.setCurrentIndex(mainn.currentIndex()+7)
#mosfet-jfet class
class mosfetx(QtWidgets.QMainWindow):
    def __init__(self):
        super(mosfetx,self).__init__()
        self.ui=mosfetmain()
        self.ui.setupUi(self)

        self.ui.btn_ara.clicked.connect(self.bulucu)
        self.ui.btn_temizle.clicked.connect(self.temiz)
        self.ui.btn_yardim.clicked.connect(self.gotuto)
        self.ui.btn_geri.clicked.connect(self.anamenu)

        self.ui.yapibox.addItem("MOSFET")
        self.ui.yapibox.addItem("JFET")
    
    def temiz(self):
        self.ui.liste3.clear()
        self.ui.label_Adet.setText("Adet: ")

        self.ui.linePolarite_2.setText("")
        self.ui.linePd_3.setText("")
        self.ui.lineVds_4.setText("")
        self.ui.lineVgs_5.setText("")
        self.ui.lineVgsth_6.setText("")
        self.ui.lineId_7.setText("")
        self.ui.lineTj_8.setText("")
        self.ui.lineQg_9.setText("")
        self.ui.linetr_10.setText("")
        self.ui.lineCd_11.setText("")
        self.ui.lineRds_12.setText("")
        self.ui.line_PaketTuru_13.setText("")
    def gotuto(self):
        mainn.setCurrentIndex(mainn.currentIndex()+1)
    def anamenu(self):
        mainn.setCurrentIndex(mainn.currentIndex()-5)
    def showError2(self):
        msg=QMessageBox()
        msg.setWindowTitle("Hata!!")
        msg.setText("Girdiğiniz değerlere ait transistör bulunamadı.\nLütfen Tekrar deneyiniz.")
        msg.setIcon(QMessageBox.Warning)

        x=msg.exec_()
    def showError3(self):
        msg=QMessageBox()
        msg.setWindowTitle("Hata!!")
        msg.setText("Lütfen internet bağlantınızı kontrol ediniz.")
        msg.setIcon(QMessageBox.Warning)

        x=msg.exec_()
    
    def bulucu(self):
      try:
        struct=self.ui.yapibox.currentText()
        polt=self.ui.linePolarite_2.text()
        Pd=self.ui.linePd_3.text()
        Vds=self.ui.lineVds_4.text()
        Vgs=self.ui.lineVgs_5.text()
        Vgsth=self.ui.lineVgsth_6.text()
        Id=self.ui.lineId_7.text()
        Tj=self.ui.lineTj_8.text()
        Qg=self.ui.lineQg_9.text()
        Tr=self.ui.linetr_10.text()
        Cd=self.ui.lineCd_11.text()
        Rds=self.ui.lineRds_12.text()
        pack=self.ui.line_PaketTuru_13.text()
        
        url = "https://alltransistors.com/mosfet/crsearch.php?struct="+struct+"&polarity="+polt+"&pd="+Pd+"+&uds="+Vds+"&ugs="+Vgs+"&ugsth="+Vgsth+"&id="+Id+"&tj="+Tj+"&qg="+Qg+"&fr="+Tr+"&cd="+Cd+"&rds="+Rds+"&caps="+pack
        html = urlopen(url)

        soup = BeautifulSoup(html, 'lxml')

        transistors=soup.find_all(target='_blank')
        str_transistors = str(transistors)
        text = BeautifulSoup(str_transistors, "lxml").get_text()
        list1=list(text[21:].split(","))

        while True:
         try:
            list1.remove("")
         except ValueError:
            break

        self.ui.liste3.clear()
        self.ui.liste3.addItems(list1)
        self.ui.label_Adet.setText(f'Adet: {str(len(list1))}')

        if self.ui.label_Adet.text()=="Adet: 0" :
            self.showError2()

      except URLError :
          self.showError3()


      return()
#igbt class
class igbtx(QtWidgets.QMainWindow):
    def __init__(self):
        super(igbtx,self).__init__()
        self.ui = igbtmain()
        self.ui.setupUi(self)

        self.ui.btn_ara.clicked.connect(self.bulucu)
        self.ui.btn_temizle.clicked.connect(self.temiz)
        self.ui.btn_tutorial.clicked.connect(self.gotuto)
        self.ui.btn_geri.clicked.connect(self.anamenu)

    def temiz(self):
        self.ui.liste2.clear()
        self.ui.lbl_adet.setText("Adet:")

        self.ui.txt_yapi.setText("")
        self.ui.txt_pc.setText("")
        self.ui.txt_vce.setText("")
        self.ui.txt_vcesat.setText("")
        self.ui.txt_veg.setText("")
        self.ui.txt_ic.setText("")
        self.ui.txt_tj.setText("")
        self.ui.txt_tr.setText("")
        self.ui.txt_cc.setText("")
        self.ui.txt_paket.setText("")
    def gotuto(self):
        mainn.setCurrentIndex(mainn.currentIndex()+1)
    def anamenu(self):
        mainn.setCurrentIndex(mainn.currentIndex()-3)
    def showError2(self):
        msg=QMessageBox()
        msg.setWindowTitle("Hata!!")
        msg.setText("Girdiğiniz değerlere ait transistör bulunamadı.\nLütfen Tekrar deneyiniz.")
        msg.setIcon(QMessageBox.Warning)

        x=msg.exec_()
    def showError3(self):
        msg=QMessageBox()
        msg.setWindowTitle("Hata!!")
        msg.setText("Lütfen internet bağlantınızı kontrol ediniz.")
        msg.setIcon(QMessageBox.Warning)

        x=msg.exec_()

    def bulucu(self):
      try:
        polt=self.ui.txt_yapi.text()
        Pc=self.ui.txt_pc.text()
        Vce=self.ui.txt_vce.text()
        Vcesat=self.ui.txt_vcesat.text()
        Veg=self.ui.txt_veg.text()
        Ic=self.ui.txt_ic.text()
        Tj=self.ui.txt_tj.text()
        Tr=self.ui.txt_tr.text()
        Cc=self.ui.txt_cc.text()
        pack=self.ui.txt_paket.text()

        url = "https://alltransistors.com/igbt/crsearch.php?struct="+polt+"&pc="+Pc+"&uce="+Vce+"&ucesat="+Vcesat+"&ueg="+Veg+"&ic="+Ic+"&tj="+Tj+"&fr="+Tr+"&cc="+Cc+"&caps="+pack
        html = urlopen(url)


        soup = BeautifulSoup(html, 'lxml')


        transistors=soup.find_all(target='_blank')
        str_transistors = str(transistors)
        text = BeautifulSoup(str_transistors, "lxml").get_text()
        list1=list(text[21:].split(","))
        
        while True:
         try:
            list1.remove("")
         except ValueError:
            break
  
       

        self.ui.liste2.clear()
        self.ui.liste2.addItems(list1)
        self.ui.lbl_adet.setText(f'Adet: {str(len(list1))}')

        if self.ui.lbl_adet.text()=="Adet: 0" :
            self.showError2()
      except URLError :
            self.showError3()
      return()
#bjt class
class bjtx(QtWidgets.QMainWindow):

    def __init__(self):
        super(bjtx, self).__init__()
        self.ui = bjtmain()
        
        self.ui.setupUi(self)
        self.ui.btn_ara.clicked.connect(self.bulucu)
        self.ui.btn_tutorial.clicked.connect(self.gotuto)
        self.ui.btn_temizle.clicked.connect(self.temiz)
        self.ui.btn_geri.clicked.connect(self.anamenu)

    def temiz(self):
        self.ui.liste_box.clear()
        self.ui.txt_adet.setText("Adet:")

        self.ui.mat_txt.setText("")
        self.ui.yapi_txt.setText("")
        self.ui.pc_txt.setText("")
        self.ui.vcb_txt.setText("")
        self.ui.vce_txt.setText("")
        self.ui.veb_txt.setText("")
        self.ui.ic_txt.setText("")
        self.ui.tj_txt.setText("")
        self.ui.ft_txt.setText("")
        self.ui.cc_txt.setText("")
        self.ui.hfe_txt.setText("")
        self.ui.caps_txt.setText("")
        self.ui.syf_edit.setText("")

    def anamenu(self):
        mainn.setCurrentIndex(mainn.currentIndex()-1)

    def gotuto(self):
        mainn.setCurrentIndex(mainn.currentIndex()+1)

    def showError(self):
          msg=QMessageBox()
          msg.setWindowTitle("Hata!!")
          msg.setText("Lütfen sayfa sayısına geçerli bir rakam giriniz!!!")
          msg.setIcon(QMessageBox.Warning)

          x=msg.exec_()

    def showError2(self):
          msg=QMessageBox()
          msg.setWindowTitle("Hata!!")
          msg.setText("Girdiğiniz değerlere ait transistör bulunamadı.\nLütfen Tekrar deneyiniz.")
          msg.setIcon(QMessageBox.Warning)

          x=msg.exec_()
    
    def showError3(self):
        msg=QMessageBox()
        msg.setWindowTitle("Hata!!")
        msg.setText("Lütfen internet bağlantınızı kontrol ediniz.")
        msg.setIcon(QMessageBox.Warning)

        x=msg.exec_()

    def bulucu(self):
      try:
        mat=self.ui.mat_txt.text()
        polt=self.ui.yapi_txt.text()
        Pc=self.ui.pc_txt.text()
        Vcb=self.ui.vcb_txt.text()
        Vce=self.ui.vce_txt.text()
        Veb=self.ui.veb_txt.text()
        Ic=self.ui.ic_txt.text()
        Tj=self.ui.tj_txt.text()
        Ft=self.ui.ft_txt.text()
        Cc=self.ui.cc_txt.text()
        hFE=self.ui.hfe_txt.text()
        pack=self.ui.caps_txt.text()
        syf=self.ui.syf_edit.text()
      
     
        url = "https://alltransistors.com/crsearch.php?mat="+mat+"&struct="+polt+"&pc="+Pc+"&ucb="+Vcb+"&uce="+Vce+"&ueb="+Veb+"&ic="+Ic+"&tj="+Tj+"&ft="+Ft+"&cc="+Cc+"&hfe="+hFE+"&caps="+pack+"&page="+str(int(syf)-1) 

        html = urlopen(url)

        soup = BeautifulSoup(html, 'lxml')

        transistors=soup.find_all(target='_blank')
        str_transistors = str(transistors)
        cleantext = BeautifulSoup(str_transistors, "lxml").get_text()
        list1=list(cleantext[21:].split(","))

        while True:
            try:
               list1.remove("")
            except ValueError:
               break
      
        self.ui.liste_box.clear()
        self.ui.liste_box.addItems(list1)
        self.ui.txt_adet.setText(f'Adet: {str(len(list1))}')
        if self.ui.txt_adet.text()=="Adet: 0" :
             self.showError2()
      except URLError :
          self.showError3()
      except ValueError:
            self.showError()
      return()      
#scr-triac class
class scrx(QtWidgets.QMainWindow):
    def __init__(self):
        super(scrx,self).__init__()
        self.ui=scrmain()
        self.ui.setupUi(self)

        self.ui.btn_ara.clicked.connect(self.bulucu)
        self.ui.btn_temizle.clicked.connect(self.temiz)
        self.ui.btn_yardim.clicked.connect(self.gotuto)
        self.ui.btn_geri.clicked.connect(self.anamenu)

    def temiz(self):
        self.ui.liste4.clear()
        self.ui.label_Adet.setText("Adet: ")

        self.ui.lineEdit_Pgm1.setText("")
        self.ui.lineEdit_Pgm2.setText("")
        self.ui.lineEdit_Vdrm1.setText("")
        self.ui.lineEdit_Vdrm2.setText("")
        self.ui.lineEdit_Itavr1.setText("")
        self.ui.lineEdit_Itavr2.setText("")
        self.ui.lineEdit_Itrms1.setText("")
        self.ui.lineEdit_Itrms2.setText("")
        self.ui.lineEdit_Itsm1.setText("")
        self.ui.lineEdit_Itsm2.setText("")
        self.ui.lineEdit_dldt1.setText("")
        self.ui.lineEdit_dldt2.setText("")
        self.ui.lineEdit_dVdt1.setText("")
        self.ui.lineEdit_dVdt2.setText("")
        self.ui.lineEdit_TstgTj.setText("")
        self.ui.lineEdit_Rthja.setText("")
        self.ui.lineEdit_Rthjc.setText("")
        self.ui.lineEdit_Vgt.setText("")
        self.ui.lineEdit_Vtm.setText("")
        self.ui.lineEdit_Igt.setText("")
        self.ui.lineEdit_Ih.setText("")
        self.ui.lineEdit_Paketturu.setText("")
    def gotuto(self):
        mainn.setCurrentIndex(mainn.currentIndex()+1)
    def anamenu(self):
        mainn.setCurrentIndex(mainn.currentIndex()-7)
    def showError2(self):
        msg=QMessageBox()
        msg.setWindowTitle("Hata!!")
        msg.setText("Girdiğiniz değerlere ait transistör bulunamadı.\nLütfen Tekrar deneyiniz.")
        msg.setIcon(QMessageBox.Warning)

        x=msg.exec_()
    def showError3(self):
        msg=QMessageBox()
        msg.setWindowTitle("Hata!!")
        msg.setText("Lütfen internet bağlantınızı kontrol ediniz.")
        msg.setIcon(QMessageBox.Warning)

        x=msg.exec_()

    def bulucu(self):
      try:
        type1=self.ui.box_type1.currentText()
        Pgm=self.ui.lineEdit_Pgm1.text()
        Pgm_max=self.ui.lineEdit_Pgm2.text()
        Vdrm=self.ui.lineEdit_Vdrm1.text()
        Vdrm_max=self.ui.lineEdit_Vdrm2.text()
        Itavr=self.ui.lineEdit_Itavr1.text()
        Itavr_max=self.ui.lineEdit_Itavr2.text()
        Itrms=self.ui.lineEdit_Itrms1.text()
        Itrms_max=self.ui.lineEdit_Itrms2.text()
        Itsm=self.ui.lineEdit_Itsm1.text()
        Itsm_max=self.ui.lineEdit_Itsm2.text()
        dIdt=self.ui.lineEdit_dldt1.text()
        dIdt_max=self.ui.lineEdit_dldt2.text()
        dVdt=self.ui.lineEdit_dVdt1.text()
        dVdt_max=self.ui.lineEdit_dVdt2.text()
        Tj=self.ui.lineEdit_TstgTj.text()
        Rth_ja=self.ui.lineEdit_Rthja.text()
        Rth_jc=self.ui.lineEdit_Rthjc.text()
        Vgt=self.ui.lineEdit_Vgt.text()
        Vtm=self.ui.lineEdit_Vtm.text()
        Igt=self.ui.lineEdit_Igt.text()
        Ih=self.ui.lineEdit_Ih.text()
        pack=self.ui.lineEdit_Paketturu.text()

        url = "https://alltransistors.com/scr/cross-reference.php?type="+type1+"&pgm="+Pgm+"&pgm_max="+Pgm_max+"&vdrm="+Vdrm+"&vdrm_max="+Vdrm_max+"&itavr="+Itavr+"&itavr_max="+Itavr_max+"+&itrms="+Itrms+"&itrms_max="+Itrms_max+"&itsm="+Itsm+"&itsm_max="+Itsm_max+"&didt="+dIdt+"&didt_max="+dIdt_max+"&dvdt="+dVdt+"&dvdt_max="+dVdt_max+"&tj="+Tj+"&rja="+Rth_ja+"&rjc="+Rth_jc+"&vgt="+Vgt+"&vtm="+Vtm+"&igt="+Igt+"&i_hold="+Ih+"&caps="+pack
        html = urlopen(url)

        soup = BeautifulSoup(html, 'lxml')

        transistors=soup.find_all('a',href=True)

        str_transistors = str(transistors)
        text = BeautifulSoup(str_transistors, "lxml").get_text()

        n=len(text)
        list1=list(text[70:n-410].split(","))
        
        while True:
         try:
            list1.remove("")
         except ValueError:
            break
        

        self.ui.liste4.clear()
        self.ui.liste4.addItems(list1)
        self.ui.label_Adet.setText(f'Adet: {str(len(list1))}')

        if self.ui.label_Adet.text()=="Adet: 0" :
            self.showError2()
      except URLError :
          self.showError3()

      return()
#bjt yardım class
class tuto(QtWidgets.QMainWindow):
    def __init__(self):
         super(tuto,self).__init__()
         self.ui=tutorial()
         self.ui.setupUi(self)
         self.ui.btn_geri.clicked.connect(self.gobjt)

    def gobjt(self):
        mainn.setCurrentIndex(mainn.currentIndex()-1)
#igbt yardım class
class tuto2(QtWidgets.QMainWindow):
    def __init__(self):
         super(tuto2,self).__init__()
         self.ui=tutorial2()
         self.ui.setupUi(self)
         self.ui.btn_geri.clicked.connect(self.goigbt)

    def goigbt(self):
        mainn.setCurrentIndex(mainn.currentIndex()-1)
#mosfet-jfet yardım class
class tuto3(QtWidgets.QMainWindow):
    def __init__(self):
         super(tuto3,self).__init__()
         self.ui=tutorial3()
         self.ui.setupUi(self)
         self.ui.btn_geri.clicked.connect(self.gomosfet)

    def gomosfet(self):
        mainn.setCurrentIndex(mainn.currentIndex()-1)
#scr-triac yardım class
class tuto4(QtWidgets.QMainWindow):
    def __init__(self):
         super(tuto4,self).__init__()
         self.ui=tutorial4()
         self.ui.setupUi(self)
         self.ui.btn_geri.clicked.connect(self.goscr)

    def goscr(self):
        mainn.setCurrentIndex(mainn.currentIndex()-1)

#Uygulama kodları
application =QtWidgets.QApplication(sys.argv)
mainn=QtWidgets.QStackedWidget()
tuto=tuto()
tuto2=tuto2()
tuto3=tuto3()
tuto4=tuto4()
mainwdw=mainwdw()
bjtx=bjtx()
igbtx=igbtx()
mosfetx=mosfetx()
scrx=scrx()
mainn.addWidget(mainwdw)
mainn.addWidget(bjtx)
mainn.addWidget(tuto)
mainn.addWidget(igbtx)
mainn.addWidget(tuto2)
mainn.addWidget(mosfetx)
mainn.addWidget(tuto3)
mainn.addWidget(scrx)
mainn.addWidget(tuto4)
mainn.setWindowIcon(QIcon("t.png"))
  
mainn.resize(610, 630)
mainn.setWindowTitle('Muadil Transistör Bulucu')
mainn.show()

try: 
   sys.exit(application.exec_())
except:
  print('Çıkış Yapılıyor')   