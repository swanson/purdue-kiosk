from mechanize import Browser
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from pymaps import Map, PyMap

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

    def showContent(self, a):
        js="document.getElementById('overlays').Buildings.click();"
        self.results.page().mainFrame().evaluateJavaScript(js)
        centerMapJs="window.scrollTo(0,100);"
        self.results.page().mainFrame().evaluateJavaScript(centerMapJs)
        self.progressBar.setVisible(False)
        self.loadingLabel.setVisible(False)
        self.results.setVisible(True)

    def hideContent(self):
        self.results.setVisible(False)
        self.progressBar.setVisible(True)
        self.loadingLabel.setVisible(True)
