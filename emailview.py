# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'directorywindow.ui'
#
# Created: Tue Sep  8 13:53:55 2009
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtWebKit import *
from emailhelper import *
import os
from flickcharm import *
from CustomListBox import *

class EmailView(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,1378,930).size()).expandedTo(Dialog.minimumSizeHint()))

        
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0,0,1381,931))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.userNameField = QLineEdit(Dialog)
        self.userNameField.setGeometry(QRect(175, 200, 100, 28))

        self.passwordField = QLineEdit(Dialog)
        self.passwordField.setGeometry(QRect(300, 200, 100, 28))
        self.passwordField.setEchoMode(QLineEdit.Password)    

        self.checkEmailButton = QPushButton(Dialog)
        self.checkEmailButton.setGeometry(QRect(450, 200, 100, 50))
        self.checkEmailButton.setText("Check email")

        self.subjectListBox = CustomListBox(Dialog)
        self.subjectListBox.setGeometry(QtCore.QRect(175,275,400,500))

        self.messageDisplay = QWebView(Dialog)
        self.messageDisplay.setGeometry(QtCore.QRect(600, 275, 600, 500))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.charm = FlickCharm()
        self.charm.activateOn(self.messageDisplay)

        self.helper = EmailHelper(Dialog, self)
        self.subjectListBox.connect(self.subjectListBox, SIGNAL("clicked(QModelIndex)"), \
                                    self.helper.displayEmail)
        self.checkEmailButton.connect(self.checkEmailButton, SIGNAL("clicked()"), \
                                    self.helper.checkEmail)

    def retranslateUi(self, Dialog):
        path = os.getcwd()
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Purdue Webmail", None, QtGui.QApplication.UnicodeUTF8))
        Dialog.setStyleSheet(QtGui.QApplication.translate("Dialog", "", None, QtGui.QApplication.UnicodeUTF8))
        self.frame.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-image: url(" + path + "/images/mockup_blank_template.png)", None, QtGui.QApplication.UnicodeUTF8))

