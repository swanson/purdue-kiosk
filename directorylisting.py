from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os

class DirectoryListing(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(535, 491)
        self.setGeometry(0, 0, 535, 491)
        self.widget = QWidget()

        self.path = os.getcwd()
        self.widget.setStyleSheet(QApplication.translate("Form", "background-image: url(" + self.path + "/images/directorylisting.png);  background-repeat:no-repeat;", None, QApplication.UnicodeUTF8))

        self.nameLabel = QLabel(self.widget)
        self.setName("Matt Swanson")
        self.nameLabel.setGeometry(QRect(190,30,400,100))
        self.nameLabel.setStyleSheet(QApplication.translate("Form", "background-image: url(null);", None, QApplication.UnicodeUTF8))

        self.emailLabel = QLabel(self.widget)
        self.setEmail("mdswanso@purdue.edu")
        self.emailLabel.setGeometry(QRect(190,98,400,100))
        self.emailLabel.setStyleSheet(QApplication.translate("Form", "background-image: url(null);", None, QApplication.UnicodeUTF8))

        self.phoneLabel = QLabel(self.widget)
        self.setPhone("123-456-7890")
        self.phoneLabel.setGeometry(QRect(190,168,400,100))
        self.phoneLabel.setStyleSheet(QApplication.translate("Form", "background-image: url(null);", None, QApplication.UnicodeUTF8))

        self.addrLabel = QTextEdit(self.widget)
        self.addrLabel.setReadOnly(True)
        self.addrLabel.viewport().setAutoFillBackground(False)
        self.addrLabel.setFrameShape(QTextEdit.NoFrame)
        self.addrLabel.setFrameShadow(QTextEdit.Plain)
        self.setAddr("123 Main Str<br>Anytown, USA 13432")
        self.addrLabel.setGeometry(QRect(190,268,270,150))
        self.addrLabel.setStyleSheet(QApplication.translate("Form", "background-image: url(null);", None, QApplication.UnicodeUTF8))

        self.univLabel = QTextEdit(self.widget)
        self.univLabel.setReadOnly(True)
        self.univLabel.viewport().setAutoFillBackground(False)
        self.univLabel.setFrameShape(QTextEdit.NoFrame)
        self.univLabel.setFrameShadow(QTextEdit.Plain)
        self.setUniv("purdue school of awesome")
        self.univLabel.setGeometry(QRect(190,345,270,150))
        self.univLabel.setStyleSheet(QApplication.translate("Form", "background-image: url(null);", None, QApplication.UnicodeUTF8))

        layout = QGridLayout(self)
        layout.addWidget(self.widget, 0, 0, -1, -1)

    def setName(self, s):
        self.nameLabel.setText(QApplication.translate("Form", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#b8860b;\">"+s+"</span></p></body></html>", None, QApplication.UnicodeUTF8))

    def setEmail(self, s):
        self.emailLabel.setText(QApplication.translate("Form", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#b8860b;\">"+s+"</span></p></body></html>", None, QApplication.UnicodeUTF8))

    def setPhone(self, s):
        self.phoneLabel.setText(QApplication.translate("Form", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#b8860b;\">"+s+"</span></p></body></html>", None, QApplication.UnicodeUTF8))

    def setAddr(self, s):
        self.addrLabel.setHtml(QApplication.translate("Form", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#b8860b;\">"+s+"</span></p></body></html>", None, QApplication.UnicodeUTF8))

    def setUniv(self, s):
        self.univLabel.setText(QApplication.translate("Form", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#b8860b;\">"+s+"</span></p></body></html>", None, QApplication.UnicodeUTF8))

    def setListing(self, listing):
        self.setName(listing.name)
        self.setEmail(listing.email)
        self.setPhone(listing.phone)
        self.setAddr(listing.addr)
        self.setUniv(listing.univ)


if __name__ == "__main__":

    import sys
    from PyQt4.QtGui import QApplication

    app = QApplication(sys.argv)
    widget = DirectoryListing()
    widget.show()
    sys.exit(app.exec_())


