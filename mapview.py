# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'directorywindow.ui'
#
# Created: Tue Sep  8 13:53:55 2009
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtWebKit import *
from maphelper import *
import os
from CustomListBox import *

class MapView(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,1024,768).size()))
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0,0,1024,768))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setObjectName("frame")

        self.resultsField = QWebView(Dialog)
        self.resultsField.setGeometry(QtCore.QRect(40,25,950,700))
        self.resultsField.setObjectName("resultsField")
        self.resultsField.settings().setAttribute(QWebSettings.JavascriptEnabled, True)
        self.resultsField.page().mainFrame().setScrollBarPolicy(Qt.Vertical, Qt.ScrollBarAlwaysOff)
        self.resultsField.page().mainFrame().setScrollBarPolicy(Qt.Horizontal, Qt.ScrollBarAlwaysOff)

        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setGeometry(QRect(240, 350, 600, 100))
        self.progressBar.setVisible(False)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(1)

        self.loadingLabel = QLabel(Dialog)
        self.loadingLabel.setGeometry(QRect(240, 190, 600, 200))
        self.loadingLabel.setText("Loading campus map...")
        self.loadingLabel.setAlignment(Qt.AlignCenter)

        self.homeButton= QPushButton(Dialog)
        self.homeButton.setGeometry(QRect(10,680,80,80))
        self.homeButton.setVisible(False)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.helper = MapHelper(Dialog, self)
        self.homeButton.connect(self.homeButton, SIGNAL("clicked()"), self.helper.close)


    def retranslateUi(self, Dialog):
        path = os.getcwd()
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Campus News", None, QtGui.QApplication.UnicodeUTF8))
        Dialog.setStyleSheet(QtGui.QApplication.translate("Dialog", "", None, QtGui.QApplication.UnicodeUTF8))
        self.frame.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-image: url(" + path + "/images/mockup_blank_template.png); background-repeat:no-repeat;", None, QtGui.QApplication.UnicodeUTF8))
        self.loadingLabel.setStyleSheet(QtGui.QApplication.translate("MainWindow", "font-size: 50px;", None, QtGui.QApplication.UnicodeUTF8))
        self.homeButton.setStyleSheet(QApplication.translate("MainWindow", "background-image: url(" + path + "/images/home.png); background-repeat:no-repeat;\n"
        "border-radius: 10px;", None, QApplication.UnicodeUTF8))


