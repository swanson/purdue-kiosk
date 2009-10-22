import sys
from PyQt4 import QtGui
from welcomeview import *
from directoryview import *
from sportsview import *
from newsview import *
from emailview import *
from mapview import *

app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
dialog = QtGui.QDialog()
ui = WelcomeView()
ui.setupUi(window)
directoryView = DirectoryView()
directoryView.setupUi(QtGui.QDialog())
sportsView = SportsView()
sportsView.setupUi(QtGui.QDialog())
newsView = NewsView()
newsView.setupUi(QtGui.QDialog())
emailView = EmailView()
emailView.setupUi(QtGui.QDialog())
mapView = MapView()
mapView.setupUi(QtGui.QDialog())


ui.directoryButton.connect(ui.directoryButton, QtCore.SIGNAL("clicked()"), directoryView.helper.showPage)
ui.sportsButton.connect(ui.sportsButton, QtCore.SIGNAL("clicked()"), sportsView.helper.showPage)
ui.newsButton.connect(ui.newsButton, QtCore.SIGNAL("clicked()"), newsView.helper.showPage)
ui.mailButton.connect(ui.mailButton, QtCore.SIGNAL("clicked()"), emailView.helper.showPage)
ui.mapButton.connect(ui.mapButton, QtCore.SIGNAL("clicked()"), mapView.helper.showPage)


window.show()
sys.exit(app.exec_())



