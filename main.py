import sys
from PyQt4 import QtGui
from welcomeview import *
from directoryview import *
from sportsview import *

app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
dialog = QtGui.QDialog()
ui = WelcomeView()
ui.setupUi(window)
directoryWindow = DirectoryVieww()
directoryWindow.setupUi(dialog)
sportsWindow = SportsView()
sportsWindow.setupUi(QtGui.QDialog())

ui.directoryButton.connect(ui.directoryButton, QtCore.SIGNAL("clicked()"), \
        directoryWindow.helper.showDirectory)
ui.sportsButton.connect(ui.sportsButton, QtCore.SIGNAL("clicked()"), \
        sportsWindow.helper.showPage)

window.show()
sys.exit(app.exec_())



