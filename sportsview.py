# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sportsview.ui'
#
# Created: Tue Sep  8 19:38:25 2009
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from sportshelper import *

class SportsView(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,1372,932).size()).expandedTo(Dialog.minimumSizeHint()))

        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0,0,1372,932))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.resultsDump = QtGui.QTextEdit(Dialog)
        self.resultsDump.setGeometry(QtCore.QRect(460,230,441,391))
        self.resultsDump.setObjectName("resultsDump")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.helper = SportsHelper(Dialog, self)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.frame.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-image: url(/home/matt/mockup_blank_template.png)", None, QtGui.QApplication.UnicodeUTF8))

