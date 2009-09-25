# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'directorywindow.ui'
#
# Created: Tue Sep  8 13:53:55 2009
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from newshelper import *
import os
from flickcharm import *
from CustomListBox import *

class NewsView(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,1378,930).size()).expandedTo(Dialog.minimumSizeHint()))

        
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0,0,1381,931))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.searchButton = QtGui.QPushButton(Dialog)
        self.searchButton.setGeometry(QtCore.QRect(420,320,80,28))
        self.searchButton.setObjectName("searchButton")

        self.resultsField = QtGui.QTextEdit(Dialog)
        self.resultsField.setGeometry(QtCore.QRect(775,275,475,500))
        self.resultsField.setObjectName("resultsField")

        self.charm = FlickCharm()
        #self.charm.activateOn(self.frame)
        self.charm.activateOn(self.resultsField)
        
        self.topicListBox = CustomListBox(Dialog)
        self.topicListBox.setGeometry(QtCore.QRect(225,275,200,500))

        self.headlineListBox = CustomListBox(Dialog)
        self.headlineListBox.setGeometry(QtCore.QRect(450,275,300,500))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.helper = NewsHelper(Dialog, self)
        self.searchButton.connect(self.searchButton, QtCore.SIGNAL("clicked()"), self.helper.doSearch)


    def retranslateUi(self, Dialog):
        path = os.getcwd()
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Campus News", None, QtGui.QApplication.UnicodeUTF8))
        Dialog.setStyleSheet(QtGui.QApplication.translate("Dialog", "", None, QtGui.QApplication.UnicodeUTF8))
        self.frame.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-image: url(" + path + "/images/mockup_blank_template.png)", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-color:white", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("Dialog", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.resultsField.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-color:white", None, QtGui.QApplication.UnicodeUTF8))

