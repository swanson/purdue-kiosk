from mechanize import Browser
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class LabHelper():
    def __init__(self, dialog, form):
        self.dialog = dialog
        self.form = form

    def showPage(self):
        self.dialog.show()
