# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'directorywindow.ui'
#
# Created: Tue Sep  8 13:53:55 2009
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from directory import *

class DirectoryWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,1378,930).size()).expandedTo(Dialog.minimumSizeHint()))

        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0,0,1381,931))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(350,250,71,18))
        self.label.setObjectName("label")

        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(350,280,71,18))
        self.label_2.setObjectName("label_2")

        self.searchButton = QtGui.QPushButton(Dialog)
        self.searchButton.setGeometry(QtCore.QRect(420,320,80,28))
        self.searchButton.setObjectName("searchButton")

        self.fnField = QtGui.QLineEdit(Dialog)
        self.fnField.setGeometry(QtCore.QRect(420,250,113,28))
        self.fnField.setObjectName("fnField")

        self.lnField = QtGui.QLineEdit(Dialog)
        self.lnField.setGeometry(QtCore.QRect(420,280,113,28))
        self.lnField.setObjectName("lnField")

        self.resultsField = QtGui.QTextEdit(Dialog)
        self.resultsField.setGeometry(QtCore.QRect(570,250,331,341))
        self.resultsField.setObjectName("resultsField")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.helper = DirectoryHelper(Dialog, self)
        self.searchButton.connect(self.searchButton, QtCore.SIGNAL("clicked()"), self.helper.doSearch)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Directory Search", None, QtGui.QApplication.UnicodeUTF8))
        Dialog.setStyleSheet(QtGui.QApplication.translate("Dialog", "bg=red", None, QtGui.QApplication.UnicodeUTF8))
        self.frame.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-image: url(/home/matt/mockup_blank_template.png)", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "First Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Last Name", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-color:white", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("Dialog", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.fnField.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-color: white", None, QtGui.QApplication.UnicodeUTF8))
        self.lnField.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-color:white", None, QtGui.QApplication.UnicodeUTF8))
        self.resultsField.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-color:white", None, QtGui.QApplication.UnicodeUTF8))

