from PyQt4.QtCore import *
from PyQt4.QtGui import *
from labhelper import *
from lablisting import *
import os

#This module allows users to view computer lab availability for all ITaP
#labs on campus, sorted by operating system (XP, Mac OS X, Solaris)

class LabView(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(QSize(QRect(0,0,1024,768).size()))
        Dialog.setWindowFlags(Qt.FramelessWindowHint)

        self.frame = QFrame(Dialog)
        self.frame.setGeometry(QRect(0,0,1024,768))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setObjectName("frame")

        self.path = os.getcwd()

        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setGeometry(QRect(240, 400, 600, 100))
        self.progressBar.setVisible(False)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(1)

        self.loadingLabel = QLabel(Dialog)
        self.loadingLabel.setGeometry(QRect(240, 190, 600, 200))
        self.loadingLabel.setText("Loading computer\nlab openings...")
        self.loadingLabel.setAlignment(Qt.AlignCenter)

        self.xpButton = QPushButton(Dialog)
        self.xpButton.setGeometry(QRect(360,90,102,102))
        self.xpButton.setIconSize(QSize(102,102))

        self.macButton = QPushButton(Dialog)
        self.macButton.setGeometry(QRect(475,90,102,102))
        self.macButton.setIconSize(QSize(102,102))

        self.sunButton = QPushButton(Dialog)
        self.sunButton.setGeometry(QRect(590,90,102,102))
        self.sunButton.setIconSize(QSize(102,102))

        self.instructions = QLabel(Dialog)
        self.instructions.setGeometry(QRect(730,60,240,160))

        img = QPixmap()
        img.load(self.path + "/images/os_text.png")
        self.instructions.setPixmap(img)
        self.instructions.setStyleSheet(QApplication.translate("MainWindow", \
        "background-image: url(null);"
        "border-radius: 15px;", None, QApplication.UnicodeUTF8))


        self.listing = LabListing(Dialog)
        self.listing.setGeometry(QRect(260,210,643,575))

        self.homeButton= QPushButton(Dialog)
        self.homeButton.setGeometry(QRect(10,680,80,80))
        self.homeButton.setVisible(False)

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

        self.helper = LabHelper(Dialog, self)

        self.xpButton.connect(self.xpButton, SIGNAL("clicked()"), \
                    self.helper.setXP)
        self.macButton.connect(self.macButton, SIGNAL("clicked()"), \
                    self.helper.setMac)
        self.sunButton.connect(self.sunButton, SIGNAL("clicked()"), \
                    self.helper.setSun)
        self.homeButton.connect(self.homeButton, SIGNAL("clicked()"), self.helper.close)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QApplication.translate("Dialog", "Computer Lab Availability", None, QApplication.UnicodeUTF8))
        Dialog.setStyleSheet(QApplication.translate("Dialog", "", None, QApplication.UnicodeUTF8))
        self.frame.setStyleSheet(QApplication.translate("Dialog", "background-image: url(" + self.path + "/images/mockup_blank_template.png); background-repeat:no-repeat;", None, QApplication.UnicodeUTF8))
        self.xpButton.setStyleSheet(QApplication.translate("MainWindow", "background-image: url(" + self.path + "/images/xp_logo.png); background-repeat:no-repeat;\n"
        "border-radius: 5px;", None, QApplication.UnicodeUTF8))
        self.macButton.setStyleSheet(QApplication.translate("MainWindow", "background-image: url(" + self.path + "/images/mac_logo.png); background-repeat:no-repeat;\n"
        "border-radius: 5px;", None, QApplication.UnicodeUTF8))
        self.sunButton.setStyleSheet(QApplication.translate("MainWindow", "background-image: url(" + self.path + "/images/sun_logo.png); background-repeat:no-repeat;\n"
        "border-radius: 5px;", None, QApplication.UnicodeUTF8))
        self.loadingLabel.setStyleSheet(QApplication.translate("MainWindow", "font-size: 50px;", None, QApplication.UnicodeUTF8))
        self.homeButton.setStyleSheet(QApplication.translate("MainWindow", "background-image: url(" + self.path + "/images/home.png);\n"
        "border-radius: 10px;", None, QApplication.UnicodeUTF8))

