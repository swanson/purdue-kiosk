# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Tue Sep  8 13:47:27 2009
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os

class WelcomeView(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,1367,978).size()).expandedTo(MainWindow.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0,0,1371,931))
        self.widget.setObjectName("widget")

        self.directoryButton = QtGui.QPushButton(self.widget)
        self.directoryButton.setGeometry(QtCore.QRect(580,220,289,281))
        self.directoryButton.setIconSize(QtCore.QSize(240,240))
        self.directoryButton.setObjectName("directoryButton")

        self.mailButton = QtGui.QPushButton(self.widget)
        self.mailButton.setGeometry(QtCore.QRect(240,220,289,281))
        self.mailButton.setIconSize(QtCore.QSize(240,240))
        self.mailButton.setObjectName("mailButton")

        self.printButton = QtGui.QPushButton(self.widget)
        self.printButton.setGeometry(QtCore.QRect(930,220,280,280))
        self.printButton.setIconSize(QtCore.QSize(240,240))
        self.printButton.setObjectName("printButton")

        self.newsButton = QtGui.QPushButton(self.widget)
        self.newsButton.setGeometry(QtCore.QRect(930,540,280,280))
        self.newsButton.setIconSize(QtCore.QSize(240,240))
        self.newsButton.setObjectName("newsButton")

        self.mapButton = QtGui.QPushButton(self.widget)
        self.mapButton.setGeometry(QtCore.QRect(580,540,292,277))
        self.mapButton.setIconSize(QtCore.QSize(240,240))
        self.mapButton.setObjectName("mapButton")

        self.sportsButton = QtGui.QPushButton(self.widget)
        self.sportsButton.setGeometry(QtCore.QRect(240,530,293,280))
        self.sportsButton.setIconSize(QtCore.QSize(240,240))
        self.sportsButton.setObjectName("sportsButton")

        self.welcomeText = QtGui.QWidget(self.widget)
        self.welcomeText.setGeometry(QtCore.QRect(780,90,471,101))
        self.welcomeText.setObjectName("welcomeText")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,1367,26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        path = os.getcwd()
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.widget.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background-image: url(" + path + "/images/mockup_blank_template.png);\n", None, QtGui.QApplication.UnicodeUTF8))
        self.directoryButton.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background-image: url(" + path + "/images/directory.png);\n"
        "border-radius: 50px;", None, QtGui.QApplication.UnicodeUTF8))
        self.mailButton.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background-image: url(" + path + "/images/mail.png);\n"
        "border-radius: 50px;", None, QtGui.QApplication.UnicodeUTF8))
        self.printButton.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background-image: url(" + path + "/images/printer.png);\n"
        "border-radius: 50px;", None, QtGui.QApplication.UnicodeUTF8))
        self.newsButton.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background-image: url(" + path + "/images/news.png);\n"
        "border-radius: 50px;", None, QtGui.QApplication.UnicodeUTF8))
        self.mapButton.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background-image: url(" + path + "/images/map.png);\n"
        "border-radius: 50px;", None, QtGui.QApplication.UnicodeUTF8))
        self.sportsButton.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background-image: url(" + path + "/images/sports.png);\n"
        "border-radius: 50px;", None, QtGui.QApplication.UnicodeUTF8))
        self.welcomeText.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background-image: url(" + path + "/images/welcome.png);", None, QtGui.QApplication.UnicodeUTF8))
