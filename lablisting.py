from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os

class LabListing(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(664, 590)
        self.setGeometry(0, 0, 664, 590)
        self.widget = QWidget()

        self.path = os.getcwd()
        self.widget.setStyleSheet(QApplication.translate("Form", "background-image: url(" + self.path + "/images/blank_lab.png); background-repeat:no-repeat;", None, QApplication.UnicodeUTF8))

        self.icon = QLabel(self.widget)
        self.icon.setGeometry(QRect(40,15,128,128))
        self.setIcon("xp")

        self.osLabel = QTextEdit(self.widget)
        self.osLabel.setReadOnly(True)
        self.osLabel.viewport().setAutoFillBackground(False)
        self.osLabel.setFrameShape(QTextEdit.NoFrame)
        self.osLabel.setFrameShadow(QTextEdit.Plain)
        self.osLabel.setGeometry(QRect(160,15,600,200))
        self.osLabel.setStyleSheet(QApplication.translate("Form", "background-image: url(null);", None, QApplication.UnicodeUTF8))

        self.labLabel = QTextEdit(self.widget)
        self.labLabel.setReadOnly(True)
        self.labLabel.viewport().setAutoFillBackground(False)
        self.labLabel.setFrameShape(QTextEdit.NoFrame)
        self.labLabel.setFrameShadow(QTextEdit.Plain)
        self.setLabs("123 Main Str<br>Anytown, USA 13432")
        self.labLabel.setGeometry(QRect(60,140,500,450))
        self.labLabel.setStyleSheet(QApplication.translate("Form", "background-image: url(null);", None, QApplication.UnicodeUTF8))

        layout = QGridLayout(self)
        layout.addWidget(self.widget, 0, 0, -1, -1)

    def setOs(self, s):
        self.osLabel.setText(QApplication.translate("Form", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; color:#b8860b;\">"+s+"<br>Workstations </span></p></body></html>", None, QApplication.UnicodeUTF8))

    def setLabs(self, s):
        self.labLabel.setHtml(QApplication.translate("Form", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#b8860b;\">"+s+"</span></p></body></html>", None, QApplication.UnicodeUTF8))

    def setIcon(self, file):
        img = QPixmap()
        img.load(self.path + "/images/" + file + "_logo.png")
        self.icon.setPixmap(img)
        self.icon.setStyleSheet(QApplication.translate("MainWindow", "background-image: url(null);"
        "border-radius: 15px;", None, QApplication.UnicodeUTF8))



if __name__ == "__main__":

    import sys
    from PyQt4.QtGui import QApplication

    app = QApplication(sys.argv)
    widget = LabListing()
    widget.show()
    sys.exit(app.exec_())
