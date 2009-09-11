# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gamescore.ui'
#
# Created: Fri Sep 11 16:56:38 2009
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class GameScore2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(QtCore.QSize(QtCore.QRect(0,0,351,531).size()).expandedTo(Form.minimumSizeHint()))

        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0,0,351,531))
        self.widget.setObjectName("widget")

        self.homeScore = QtGui.QLabel(self.widget)
        self.homeScore.setGeometry(QtCore.QRect(220,70,71,71))
        self.homeScore.setObjectName("homeScore")

        self.awayScore = QtGui.QLabel(self.widget)
        self.awayScore.setGeometry(QtCore.QRect(220,160,71,71))
        self.awayScore.setObjectName("awayScore")

        self.awayTeam = QtGui.QLabel(self.widget)
        self.awayTeam.setGeometry(QtCore.QRect(50,160,101,71))
        self.awayTeam.setObjectName("awayTeam")

        self.date = QtGui.QLabel(self.widget)
        self.date.setGeometry(QtCore.QRect(110,440,221,71))
        self.date.setObjectName("date")

        self.headline = QtGui.QLabel(self.widget)
        self.headline.setGeometry(QtCore.QRect(50,250,261,181))
        self.headline.setObjectName("headline")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.widget.setStyleSheet(QtGui.QApplication.translate("Form", "background-image: url(/home/matt/score.png);", None, QtGui.QApplication.UnicodeUTF8))
        self.homeScore.setStyleSheet(QtGui.QApplication.translate("Form", "background-image: url(null);", None, QtGui.QApplication.UnicodeUTF8))
        self.homeScore.setText(QtGui.QApplication.translate("Form", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:29pt; color:#b8860b;\">53</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.awayScore.setStyleSheet(QtGui.QApplication.translate("Form", "background-image: url(null);", None, QtGui.QApplication.UnicodeUTF8))
        self.awayScore.setText(QtGui.QApplication.translate("Form", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:29pt; color:#b8860b;\">10</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.awayTeam.setStyleSheet(QtGui.QApplication.translate("Form", "background-image: url(null);", None, QtGui.QApplication.UnicodeUTF8))
        self.awayTeam.setText(QtGui.QApplication.translate("Form", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:29pt; color:#b8860b;\">ORE</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.date.setStyleSheet(QtGui.QApplication.translate("Form", "background-image: url(null);", None, QtGui.QApplication.UnicodeUTF8))
        self.date.setText(QtGui.QApplication.translate("Form", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:29pt; color:#b8860b;\">Sept 5</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.headline.setStyleSheet(QtGui.QApplication.translate("Form", "background-image: url(null);", None, QtGui.QApplication.UnicodeUTF8))
        self.headline.setText(QtGui.QApplication.translate("Form", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:29pt; color:#b8860b;\">Extra info</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:29pt; color:#b8860b;\">line 2</p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:29pt; color:#b8860b;\">ln 3</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
if __name__ == "__main__":

    import sys
    from PyQt4.QtGui import QApplication

    app = QApplication(sys.argv)
    widget = GameScore2()
    widget.show()
    sys.exit(app.exec_())
