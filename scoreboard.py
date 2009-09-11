from PyQt4 import QtGui, QtCore

class Scoreboard(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        
        self.setFixedSize(371, 551)
        self.setGeometry(0, 0, 371, 551)
        self.widget = QtGui.QWidget()        

        self.awayLabel = QtGui.QLabel(self.tr("Away team"))
        self.awayLabel.setObjectName("awayLabel")

        self.awayScoreLabel = QtGui.QLabel(self.tr("0"))
        self.awayScoreLabel.setObjectName("awayScoreLabel")

        self.homeScoreLabel = QtGui.QLabel(self.tr("10"))
        self.homeScoreLabel.setObjectName("homeScoreLabel")

        self.dateLabel = QtGui.QLabel(self.tr("Jan 1, 1900"))
        self.dateLabel.setObjectName("dateLabel")

        self.headlineLabel = QtGui.QLabel(self.tr("test"))
        self.headlineLabel.setObjectName("headlineLabel")

        self.widget.setStyleSheet(QtGui.QApplication.translate("Form", "background-image: url(/home/matt/score.png);", None, QtGui.QApplication.UnicodeUTF8))
        
        self.homeScoreLabel.setStyleSheet(QtGui.QApplication.translate("Form", "background-image: url(null);", None, QtGui.QApplication.UnicodeUTF8))
        self.homeScoreLabel.setText(QtGui.QApplication.translate("Form", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:29pt; color        :#b8860b;\">53</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

        self.awayScoreLabel.setStyleSheet(QtGui.QApplication.translate("Form", "background-image: url(null);", None, QtGui.QApplication.UnicodeUTF8))
        self.awayScoreLabel.setText(QtGui.QApplication.translate("Form", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:29pt; color:#b8860b;\">10</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.awayLabel.setStyleSheet(QtGui.QApplication.translate("Form", "background-image: url(null);", None, QtGui.QApplication.UnicodeUTF8))
        self.awayLabel.setText(QtGui.QApplication.translate("Form", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:29pt; color:#b8860b;\">ORE</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.dateLabel.setStyleSheet(QtGui.QApplication.translate("Form", "background-image: url(null);", None, QtGui.QApplication.UnicodeUTF8))
        self.dateLabel.setText(QtGui.QApplication.translate("Form", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:29pt; color:#b8860b;\">Sept 5</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.headlineLabel.setStyleSheet(QtGui.QApplication.translate("Form", "background-image: url(null);", None, QtGui.QApplication.UnicodeUTF8))
        self.headlineLabel.setText(QtGui.QApplication.translate("Form", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:29pt; color:#b8860b;\">Extra info</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:29pt; color:#b8860b;\">line 2</p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:29pt; color:#b8860b;\">ln 3</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))




        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.widget, 0, 0, -1, -1)
        layout.addWidget(self.homeScoreLabel, 0, 1, 1, 1, QtCore.Qt.AlignCenter)
        layout.addWidget(self.awayScoreLabel, 1, 1, 1, 1, QtCore.Qt.AlignCenter)
        layout.addWidget(self.awayLabel, 1, 0, 1, 1, QtCore.Qt.AlignCenter)
        layout.addWidget(self.headlineLabel, 2, 0, 1, 2, QtCore.Qt.AlignCenter)
        layout.addWidget(self.dateLabel, 3, 0, 1, 2, QtCore.Qt.AlignCenter)

        layout.setRowMinimumHeight(0, 150)

    def homeScore(self):
        return self.homeScoreLabel.text()

    def setHomeScore(self, score):
        self.homeScoreLabel.setText(score)

    def awayScore(self):
        return self.awayScoreLabel.text()

    def setAwayScore(self, score):
        self.awayScoreLabel.setText(score)

    def awayTeam(self):
        return self.awayLabel.text()

    def setAwayTeam(self, team):
        self.awayLabel.setText(text)

    def date(self):
        return self.dateLabel.text()

    def setDate(self, datestr):
        self.dateLabel.setText(datestr)

    def headline(self):
        return self.headlineLabel.text()

    def setHeadline(self, hl):
        self.headlineLabel.setText(hl)

if __name__ == "__main__":

    import sys
    from PyQt4.QtGui import QApplication

    app = QApplication(sys.argv)
    widget = Scoreboard()
    widget.show()
    sys.exit(app.exec_())


