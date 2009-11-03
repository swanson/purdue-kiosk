# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'directorywindow.ui'
#
# Created: Tue Sep  8 13:53:55 2009
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtWebKit import *
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

        self.resultsField = QWebView(Dialog)
        self.resultsField.setGeometry(QtCore.QRect(725,125,560,700))
        self.resultsField.setTextSizeMultiplier(2)
        self.resultsField.setObjectName("resultsField")
        #self.resultsField.settings().setAttribute(QWebSettings.JavascriptEnabled, False)

        self.charm = FlickCharm()
        #self.charm.activateOn(self.frame)
        self.charm.activateOn(self.resultsField)

        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setGeometry(QRect(450, 450, 600, 100))
        self.progressBar.setVisible(False)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(1)

        self.loadingLabel = QLabel(Dialog)
        self.loadingLabel.setGeometry(QRect(450, 350, 600, 100))
        self.loadingLabel.setText("Loading news feeds...")
        self.loadingLabel.setAlignment(Qt.AlignCenter)

        self.topicListBox = CustomListBox(Dialog)
        self.topicListBox.setGeometry(QtCore.QRect(175,275,200,500))

        self.headlineListBox = CustomListBox(Dialog)
        self.headlineListBox.setGeometry(QtCore.QRect(400,275,300,500))

        self.homeButton= QPushButton(Dialog)
        self.homeButton.setGeometry(QRect(10,750,100,100))
        self.homeButton.setVisible(False)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.helper = NewsHelper(Dialog, self)
        self.topicListBox.connect(self.topicListBox, SIGNAL("clicked(QModelIndex)"), \
                                    self.helper.populateHeadlineList)
        self.headlineListBox.connect(self.headlineListBox, SIGNAL("clicked(QModelIndex)"), \
                                        self.helper.displayStory)
        self.homeButton.connect(self.homeButton, SIGNAL("clicked()"), self.helper.close)


    def retranslateUi(self, Dialog):
        path = os.getcwd()
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Campus News", None, QtGui.QApplication.UnicodeUTF8))
        Dialog.setStyleSheet(QtGui.QApplication.translate("Dialog", "", None, QtGui.QApplication.UnicodeUTF8))
        self.frame.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-image: url(" + path + "/images/mockup_blank_template.png)", None, QtGui.QApplication.UnicodeUTF8))
        self.loadingLabel.setStyleSheet(QtGui.QApplication.translate("MainWindow", "font-size: 50px;", None, QtGui.QApplication.UnicodeUTF8))
        self.homeButton.setStyleSheet(QApplication.translate("MainWindow", "background-image: url(" + path + "/images/home.png);\n"
        "border-radius: 10px;", None, QApplication.UnicodeUTF8))


