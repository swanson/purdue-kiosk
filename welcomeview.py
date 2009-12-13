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
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,1024,768).size()))
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setFocus()

        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0,0,1024,768))
        self.widget.setObjectName("widget")

        self.mailButton = QtGui.QPushButton(self.widget)
        self.mailButton.setGeometry(QtCore.QRect(140,200,200,200))
        self.mailButton.setIconSize(QtCore.QSize(240,240))
        self.mailButton.setObjectName("mailButton")

        self.directoryButton = QtGui.QPushButton(self.widget)
        self.directoryButton.setGeometry(QtCore.QRect(420,200,200,200))
        self.directoryButton.setIconSize(QtCore.QSize(200,200))
        self.directoryButton.setObjectName("directoryButton")

        self.labButton = QtGui.QPushButton(self.widget)
        self.labButton.setGeometry(QtCore.QRect(700,200,200,200))
        self.labButton.setIconSize(QtCore.QSize(240,240))
        self.labButton.setObjectName("labButton")

        self.sportsButton = QtGui.QPushButton(self.widget)
        self.sportsButton.setGeometry(QtCore.QRect(140,450,200,200))
        self.sportsButton.setIconSize(QtCore.QSize(240,240))
        self.sportsButton.setObjectName("sportsButton")

        self.mapButton = QtGui.QPushButton(self.widget)
        self.mapButton.setGeometry(QtCore.QRect(420,450,200,200))
        self.mapButton.setIconSize(QtCore.QSize(240,240))
        self.mapButton.setObjectName("mapButton")

        self.newsButton = QtGui.QPushButton(self.widget)
        self.newsButton.setGeometry(QtCore.QRect(700,450,200,200))
        self.newsButton.setIconSize(QtCore.QSize(240,240))
        self.newsButton.setObjectName("newsButton")

        self.welcomeText = QtGui.QWidget(self.widget)
        self.welcomeText.setGeometry(QtCore.QRect(570,65,471,101))
        self.welcomeText.setObjectName("welcomeText")
        MainWindow.setCentralWidget(self.centralwidget)

        #temp button to close program while testing without border
        self.exit = QtGui.QPushButton(self.widget)
        self.exit.setGeometry(QtCore.QRect(20,710, 60, 30))
        self.exit.setText("exit")
        #self.exit.setVisible(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        path = os.getcwd()
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.widget.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background-image: url(" + path + "/images/mockup_blank_template.png); background-repeat:no-repeat;\n", None, QtGui.QApplication.UnicodeUTF8))
        self.directoryButton.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background-image: url(" + path + "/images/directory.png); background-repeat:no-repeat;\n"
        "border-radius: 5px;", None, QtGui.QApplication.UnicodeUTF8))
        self.mailButton.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background-image: url(" + path + "/images/mail.png); background-repeat:no-repeat;\n"
        "border-radius: 5px;", None, QtGui.QApplication.UnicodeUTF8))
        self.labButton.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background-image: url(" + path + "/images/itap.png); background-repeat:no-repeat;\n"
        "border-radius: 5px;", None, QtGui.QApplication.UnicodeUTF8))
        self.newsButton.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background-image: url(" + path + "/images/news.png); background-repeat:no-repeat;\n"
        "border-radius: 5px;", None, QtGui.QApplication.UnicodeUTF8))
        self.mapButton.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background-image: url(" + path + "/images/map.png); background-repeat:no-repeat;\n"
        "border-radius: 5px;", None, QtGui.QApplication.UnicodeUTF8))
        self.sportsButton.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background-image: url(" + path + "/images/sports.png); background-repeat:no-repeat;\n"
        "border-radius: 5px;", None, QtGui.QApplication.UnicodeUTF8))
        self.welcomeText.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background-image: url(" + path + "/images/welcome.png); background-repeat:no-repeat;", None, QtGui.QApplication.UnicodeUTF8))
