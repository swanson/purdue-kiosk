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

        self.path = os.getcwd()


        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setGeometry(QRect(450, 450, 600, 100))
        self.progressBar.setVisible(False)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(1)

        self.loadingLabel = QLabel(Dialog)
        self.loadingLabel.setGeometry(QRect(450, 250, 600, 200))
        self.loadingLabel.setText("Loading computer\nlab openings...")
        self.loadingLabel.setAlignment(Qt.AlignCenter)

        self.xpButton = QPushButton(Dialog)
        self.xpButton.setGeometry(QRect(520,120,128,128))
        self.xpButton.setIconSize(QSize(128,128))

        self.macButton = QPushButton(Dialog)
        self.macButton.setGeometry(QRect(660,120,128,128))
        self.macButton.setIconSize(QSize(128,128))

        self.sunButton = QPushButton(Dialog)
        self.sunButton.setGeometry(QRect(800,120,128,128))
        self.sunButton.setIconSize(QSize(128,128))

        self.instructions = QLabel(Dialog)
        self.instructions.setGeometry(QRect(1000,100,240,160))

        img = QPixmap()
        img.load(self.path + "/images/os_text.png")
        self.instructions.setPixmap(img)
        self.instructions.setStyleSheet(QApplication.translate("MainWindow", \
        "background-image: url(null);"
        "border-radius: 15px;", None, QApplication.UnicodeUTF8))


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
        Dialog.setWindowTitle(QApplication.translate("Dialog", "Computer Lab Availability", None, QApplication.UnicodeUTF8))
        Dialog.setStyleSheet(QApplication.translate("Dialog", "", None, QApplication.UnicodeUTF8))
        self.frame.setStyleSheet(QApplication.translate("Dialog", "background-image: url(" + self.path + "/images/mockup_blank_template.png)", None, QApplication.UnicodeUTF8))
        self.xpButton.setStyleSheet(QApplication.translate("MainWindow", "background-image: url(" + self.path + "/images/xp_logo.png);\n"
        "border-radius: 15px;", None, QApplication.UnicodeUTF8))
        self.macButton.setStyleSheet(QApplication.translate("MainWindow", "background-image: url(" + self.path + "/images/mac_logo.png);\n"
        "border-radius: 15px;", None, QApplication.UnicodeUTF8))
        self.sunButton.setStyleSheet(QApplication.translate("MainWindow", "background-image: url(" + self.path + "/images/sun_logo.png);\n"
        "border-radius: 15px;", None, QApplication.UnicodeUTF8))
        self.loadingLabel.setStyleSheet(QApplication.translate("MainWindow", "font-size: 50px;", None, QApplication.UnicodeUTF8))