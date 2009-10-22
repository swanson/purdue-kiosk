# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'directorywindow.ui'
#
# Created: Tue Sep  8 13:53:55 2009
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from labhelper import *
from lablisting import *
import os

class LabView(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(QSize(QRect(0,0,1378,930).size()).expandedTo(Dialog.minimumSizeHint()))


        self.frame = QFrame(Dialog)
        self.frame.setGeometry(QRect(0,0,1381,931))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")

        self.xpButton = QPushButton(Dialog)
        self.xpButton.setGeometry(QRect(520,120,128,128))
        self.xpButton.setIconSize(QSize(128,128))

        self.macButton = QPushButton(Dialog)
        self.macButton.setGeometry(QRect(660,120,128,128))
        self.macButton.setIconSize(QSize(128,128))

        self.sunButton = QPushButton(Dialog)
        self.sunButton.setGeometry(QRect(800,120,128,128))
        self.sunButton.setIconSize(QSize(128,128))

        #path = os.getcwd()
        #self.os = QImage(Dialog)
        #self.os.setGeometry(QRect(900, 120, 300, 300))
        #self.os.load(path+"/images/os_text.png")

        self.listing = LabListing(Dialog)
        self.listing.setGeometry(QRect(400,260,643,575))

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

        self.helper = LabHelper(Dialog, self)

        self.xpButton.connect(self.xpButton, SIGNAL("clicked()"), \
                    self.helper.setXP)
        self.macButton.connect(self.macButton, SIGNAL("clicked()"), \
                    self.helper.setMac)
        self.sunButton.connect(self.sunButton, SIGNAL("clicked()"), \
                    self.helper.setSun)

    def retranslateUi(self, Dialog):
        path = os.getcwd()
        Dialog.setWindowTitle(QApplication.translate("Dialog", "Computer Lab Availability", None, QApplication.UnicodeUTF8))
        Dialog.setStyleSheet(QApplication.translate("Dialog", "", None, QApplication.UnicodeUTF8))
        self.frame.setStyleSheet(QApplication.translate("Dialog", "background-image: url(" + path + "/images/mockup_blank_template.png)", None, QApplication.UnicodeUTF8))
        self.xpButton.setStyleSheet(QApplication.translate("MainWindow", "background-image: url(" + path + "/images/xp_logo.png);\n"
        "border-radius: 15px;", None, QApplication.UnicodeUTF8))
        self.macButton.setStyleSheet(QApplication.translate("MainWindow", "background-image: url(" + path + "/images/mac_logo.png);\n"
        "border-radius: 15px;", None, QApplication.UnicodeUTF8))
        self.sunButton.setStyleSheet(QApplication.translate("MainWindow", "background-image: url(" + path + "/images/sun_logo.png);\n"
        "border-radius: 15px;", None, QApplication.UnicodeUTF8))



