from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os

class Scoreboard(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)

        self.setFixedSize(371, 551)
        self.setGeometry(0, 0, 371, 551)
        self.widget = QWidget()

        self.awayLabel = QTextEdit(self.widget)
        self.awayLabel.setReadOnly(True)
        self.awayLabel.viewport().setAutoFillBackground(False)
        self.awayLabel.setFrameShape(QTextEdit.NoFrame)
        self.awayLabel.setFrameShadow(QTextEdit.Plain)
        self.awayLabel.setGeometry(QRect(15,150,160,150))

        self.awayScoreLabel = QLabel(self.widget)
        self.awayScoreLabel.setGeometry(QRect(180,100,100,150))

        self.homeScoreLabel = QLabel(self.widget)
        self.homeScoreLabel.setGeometry(QRect(180,5,200,150))

        self.dateLabel = QLabel(self.widget)
        self.dateLabel.setGeometry(QRect(90,280,300,150))

        self.headlineLabel = QLabel(self.widget)
        self.headlineLabel.setGeometry(QRect(50,215,300,150))

        self.path = os.getcwd()
        self.widget.setStyleSheet(QApplication.translate("Form", "background-image: url(" + self.path + "/images/score.png); background-repeat:no-repeat;", None, QApplication.UnicodeUTF8))

        self.homeScoreLabel.setStyleSheet(QApplication.translate("Form", "background-image: url(null);", None, QApplication.UnicodeUTF8))
        self.setHomeScore('10')

        self.awayScoreLabel.setStyleSheet(QApplication.translate("Form", "background-image: url(null);", None, QApplication.UnicodeUTF8))
        self.setAwayScore('37')

        self.awayLabel.setStyleSheet(QApplication.translate("Form", "background-image: url(null);", None, QApplication.UnicodeUTF8))
        self.setAwayTeam('Minnesota')

        self.dateLabel.setStyleSheet(QApplication.translate("Form", "background-image: url(null);", None, QApplication.UnicodeUTF8))
        self.setDate('09/01')

        self.headlineLabel.setStyleSheet(QApplication.translate("Form", "background-image: url(null);", None, QApplication.UnicodeUTF8))
        self.setHeadline('Purdue wins <br /> Hooray!')

        layout = QGridLayout(self)
        layout.addWidget(self.widget, 0, 0, -1, -1)

    def homeScore(self):
        return self.homeScoreLabel.text()

    def setHomeScore(self, score):
        self.homeScoreLabel.setText(QApplication.translate("Form", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\"font-size:45pt; color:#b8860b\">"+score+"</span></p></body></html>", None, QApplication.UnicodeUTF8))

    def awayScore(self):
        return self.awayScoreLabel.text()

    def setAwayScore(self, score):
         self.awayScoreLabel.setText(QApplication.translate("Form", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:45pt; color:#b8860b;\">"+score+"</span></p></body></html>", None, QApplication.UnicodeUTF8))


    def awayTeam(self):
        return self.awayLabel.text()

    def setAwayTeam(self, team):
        self.awayLabel.setText(QApplication.translate("Form", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#b8860b;\">" + team + "</span></p></body></html>", None, QApplication.UnicodeUTF8))


    def date(self):
        return self.dateLabel.text()

    def setDate(self, datestr):
        self.dateLabel.setText(QApplication.translate("Form", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#b8860b;\">"+datestr+"</span></p></body></html>", None, QApplication.UnicodeUTF8))

    def headline(self):
        return self.headlineLabel.text()

    def setHeadline(self, hl):
        self.headlineLabel.setText(QApplication.translate("Form", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#b8860b;\">"+hl+"</span></p>\n"
        , None, QApplication.UnicodeUTF8))

if __name__ == "__main__":

    import sys
    from PyQt4.QtGui import QApplication

    app = QApplication(sys.argv)
    widget = Scoreboard()
    widget.show()
    sys.exit(app.exec_())


