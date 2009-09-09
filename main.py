import sys
from PyQt4 import QtGui
from gui_test import *
from directory import *
from directorywindow import *
from sportsview import *

app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
dialog = QtGui.QDialog()
ui = Ui_MainWindow()
ui.setupUi(window)
directoryWindow = DirectoryWindow()
directoryWindow.setupUi(dialog)
sportsWindow = SportsView()
sportsWindow.setupUi(QtGui.QDialog())

ui.directoryButton.connect(ui.directoryButton, QtCore.SIGNAL("clicked()"), \
        directoryWindow.helper.showDirectory)
ui.sportsButton.connect(ui.sportsButton, QtCore.SIGNAL("clicked()"), \
        sportsWindow.helper.showPage)

window.show()
sys.exit(app.exec_())



