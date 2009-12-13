from mechanize import Browser
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup
import sys, os
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#This module allows users to view an interactive campus map
#through a Google Maps window

class MapHelper():
    def __init__(self, dialog, form):
        self.dialog = dialog
        self.form = form
        self.progressBar = form.progressBar
        self.loadingLabel = form.loadingLabel
        self.results = self.form.resultsField

    def showPage(self):
        self.dialog.show()
        self.hideContent();
        self.results.load(QUrl("http://www.purdue.edu/Campus_Map"))
        self.dialog.connect(self.results, \
                    SIGNAL("loadFinished(bool)"), self.showContent)

    def close(self):
        self.dialog.close()

    def showContent(self, a):
        path = os.getcwd()
        self.form.frame.setStyleSheet(QApplication.translate("Dialog", \
        "background-image: url(" + path + "/images/map_bg.png); background-repeat:no-repeat;", \
        None, QApplication.UnicodeUTF8))
        js=" if (document.getElementById('overlays').Buildings.checked) \
             { \
	            document.getElementById('overlays').Buildings.click(); \
             }"
        self.results.page().mainFrame().evaluateJavaScript(js)
        centerMapJs="window.scrollTo(0,100);"
        self.results.page().mainFrame().evaluateJavaScript(centerMapJs)
        self.progressBar.setVisible(False)
        self.loadingLabel.setVisible(False)
        self.results.setVisible(True)
        self.form.homeButton.setVisible(True)

    def hideContent(self):
        self.results.setVisible(False)
        self.progressBar.setVisible(True)
        self.loadingLabel.setVisible(True)
        self.form.homeButton.setVisible(False)
