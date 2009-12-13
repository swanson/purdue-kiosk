from PyQt4 import QtCore, QtGui
from sportshelper import *
from scoreboard import *
import os

#This module allows users to view Purdue football scores for the whole season
#as well as the teams record after each games and the start times and dates
#for future games

class SportsView(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,1024,768).size()))
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0,0,1024,768))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setObjectName("frame")

        self.score1 = Scoreboard(Dialog)
        self.score1.setGeometry(QtCore.QRect(115,230,self.score1.width(),self.score1.height()))

        self.score2 = Scoreboard(Dialog)
        self.score2.setGeometry(QtCore.QRect(400,230,self.score1.width(),self.score1.height()))

        self.score3 = Scoreboard(Dialog)
        self.score3.setGeometry(QtCore.QRect(685,230,self.score1.width(),self.score1.height()))

        self.backButton = QtGui.QPushButton(Dialog)
        self.backButton.setGeometry(QtCore.QRect(290,100,128,128))
        self.backButton.setIconSize(QtCore.QSize(240,240))
        self.backButton.setObjectName("backButton")

        self.forward = QtGui.QPushButton(Dialog)
        self.forward.setGeometry(QtCore.QRect(670, 100, 128, 128))
        self.forward.setIconSize(QtCore.QSize(240, 240))
        self.forward.setObjectName("forward")

        self.homeButton= QtGui.QPushButton(Dialog)
        self.homeButton.setGeometry(QtCore.QRect(10,680,80,80))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.helper = SportsHelper(Dialog, self)

        self.backButton.connect(self.backButton, QtCore.SIGNAL("clicked()"), \
            self.helper.shiftLeft)
        self.forward.connect(self.forward, QtCore.SIGNAL("clicked()"), \
            self.helper.shiftRight)
        self.homeButton.connect(self.homeButton, QtCore.SIGNAL("clicked()"), self.helper.close)


    def retranslateUi(self, Dialog):
        path = os.getcwd()
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.frame.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-image: url(" + path + "/images/mockup_blank_template.png); background-repeat:no-repeat;", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-image: url(" + path + "/images/back_arrow.png); background-repeat:no-repeat;\n" "border-radius: 1px;", None, QtGui.QApplication.UnicodeUTF8))
        self.forward.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-image: url(" + path + "/images/forward_arrow.png); background-repeat:no-repeat;\n" "border-radius: 1px;", None, QtGui.QApplication.UnicodeUTF8))
        self.homeButton.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background-image: url(" + path + "/images/home.png); background-repeat:no-repeat;\n"
        "border-radius: 10px;", None, QtGui.QApplication.UnicodeUTF8))

