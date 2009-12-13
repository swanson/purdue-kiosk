from PyQt4 import QtCore, QtGui
from directoryhelper import *
import os
from CustomListBox import *
from directorylisting import *

#This module allows the user to search for students and faculty using the Purdue
#LDAP (Lightweight Directory Access Protocol) directory


class DirectoryView(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,1024,768).size()))
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0,0,1024,768))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setObjectName("frame")

        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(285,70,100,100))
        self.label.setObjectName("label")

        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(535,70,100,100))
        self.label_2.setObjectName("label_2")

        self.searchButton = QtGui.QPushButton(Dialog)
        self.searchButton.setGeometry(QtCore.QRect(800,100,150,50))
        self.searchButton.setObjectName("searchButton")

        self.fnField = QtGui.QLineEdit(Dialog)
        self.fnField.setGeometry(QtCore.QRect(375,100,150,50))
        self.fnField.setObjectName("fnField")

        self.lnField = QtGui.QLineEdit(Dialog)
        self.lnField.setGeometry(QtCore.QRect(625,100,150,50))
        self.lnField.setObjectName("lnField")

        self.results = CustomListBox(Dialog)
        self.results.setGeometry(QtCore.QRect(125,200,300,500))

        self.listing = DirectoryListing(Dialog)
        self.listing.setGeometry(QtCore.QRect(435, 200, 555, 491))

        self.homeButton= QtGui.QPushButton(Dialog)
        self.homeButton.setGeometry(QtCore.QRect(10,680,80,80))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.helper = DirectoryHelper(Dialog, self)
        self.searchButton.connect(self.searchButton, QtCore.SIGNAL("clicked()"), self.helper.doSearch)
        self.results.connect(self.results, SIGNAL("clicked(QModelIndex)"), \
                                    self.helper.displayInfo)
        self.homeButton.connect(self.homeButton, SIGNAL("clicked()"), self.helper.close)


    def retranslateUi(self, Dialog):
        path = os.getcwd()
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Directory Search", None, QtGui.QApplication.UnicodeUTF8))
        Dialog.setStyleSheet(QtGui.QApplication.translate("Dialog", "bg=red", None, QtGui.QApplication.UnicodeUTF8))
        self.frame.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-image: url(" + path + "/images/mockup_blank_template.png);  background-repeat:no-repeat;", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "First<br>Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setStyleSheet(QtGui.QApplication.translate("Dialog", "font-size: 20pt; text-align: center;", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Last<br>Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setStyleSheet(QtGui.QApplication.translate("Dialog", "font-size: 20pt; text-align: center;", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-color:white", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("Dialog", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-color: #a0a0a0; color: #b8860b; font-size: 20pt", None, QtGui.QApplication.UnicodeUTF8))
        self.fnField.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-color: white; font-size: 20pt", None, QtGui.QApplication.UnicodeUTF8))
        self.lnField.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-color:white; font-size: 20pt", None, QtGui.QApplication.UnicodeUTF8))
        self.homeButton.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background-image: url(" + path + "/images/home.png);\n"
        "border-radius: 10px;", None, QtGui.QApplication.UnicodeUTF8))

