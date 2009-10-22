# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'directorywindow.ui'
#
# Created: Tue Sep  8 13:53:55 2009
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from labhelper import *
import os

class LabView(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,1378,930).size()).expandedTo(Dialog.minimumSizeHint()))


        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0,0,1381,931))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.helper = LabHelper(Dialog, self)

    def retranslateUi(self, Dialog):
        path = os.getcwd()
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Computer Lab Availability", None, QtGui.QApplication.UnicodeUTF8))
        Dialog.setStyleSheet(QtGui.QApplication.translate("Dialog", "", None, QtGui.QApplication.UnicodeUTF8))
        self.frame.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-image: url(" + path + "/images/mockup_blank_template.png)", None, QtGui.QApplication.UnicodeUTF8))

