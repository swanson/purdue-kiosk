from PyQt4 import QtCore, QtGui
from PyQt4.QtWebKit import *
from emailhelper import *
import os
from flickcharm import *
from CustomListBox import *

#This module is responsible for allowing students to read messages in their
#Purdue email inbox.

class EmailView(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,1024,768).size()))
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0,0,1024,768))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setObjectName("frame")

        self.userNameField = QLineEdit(Dialog)
        self.userNameField.setGeometry(QRect(300, 100, 200, 50))

        self.passwordField = QLineEdit(Dialog)
        self.passwordField.setGeometry(QRect(550, 100, 200, 50))
        self.passwordField.setEchoMode(QLineEdit.Password)

        self.checkEmailButton = QPushButton(Dialog)
        self.checkEmailButton.setGeometry(QRect(800, 100, 100, 50))
        self.checkEmailButton.setText("Check email")

        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setGeometry(QRect(240, 400, 600, 100))
        self.progressBar.setVisible(False)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(1)

        self.loadingLabel = QLabel(Dialog)
        self.loadingLabel.setGeometry(QRect(240, 190, 600, 200))
        self.loadingLabel.setText("Loading emails...")
        self.loadingLabel.setAlignment(Qt.AlignCenter)

        self.subjectListBox = CustomListBox(Dialog)
        self.subjectListBox.setGeometry(QtCore.QRect(125,200,300,500))

        self.messageDisplay = QWebView(Dialog)
        self.messageDisplay.setGeometry(QtCore.QRect(435, 200, 500, 500))
        self.messageDisplay.setVisible(False)

        self.homeButton= QtGui.QPushButton(Dialog)
        self.homeButton.setGeometry(QtCore.QRect(10,680,80,80))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.charm = FlickCharm()
        self.charm.activateOn(self.messageDisplay)

        self.helper = EmailHelper(Dialog, self)
        self.subjectListBox.connect(self.subjectListBox, SIGNAL("clicked(QModelIndex)"), \
                                    self.helper.displayEmail)
        self.checkEmailButton.connect(self.checkEmailButton, SIGNAL("clicked()"), \
                                    self.helper.checkEmail)
        self.homeButton.connect(self.homeButton, SIGNAL("clicked()"), self.helper.close)

    def retranslateUi(self, Dialog):
        path = os.getcwd()
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Purdue Webmail", None, QtGui.QApplication.UnicodeUTF8))
        Dialog.setStyleSheet(QtGui.QApplication.translate("Dialog", "", None, QtGui.QApplication.UnicodeUTF8))
        self.frame.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-image: url(" + path + "/images/mockup_blank_template.png); background-repeat:no-repeat;", None, QtGui.QApplication.UnicodeUTF8))
        self.homeButton.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background-image: url(" + path + "/images/home.png); background-repeat:no-repeat;\n"
        "border-radius: 10px;", None, QtGui.QApplication.UnicodeUTF8))
        self.userNameField.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-color: white; font-size: 20pt", None, QtGui.QApplication.UnicodeUTF8))
        self.passwordField.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-color:white; font-size: 20pt", None, QtGui.QApplication.UnicodeUTF8))
        self.loadingLabel.setStyleSheet(QApplication.translate("MainWindow", "font-size: 50px;", None, QApplication.UnicodeUTF8))
