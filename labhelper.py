from mechanize import Browser
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import urllib


class LabHelper():
    def __init__(self, dialog, form):
        self.dialog = dialog
        self.form = form
        self.listing = form.listing
        self.xpLabs = []
        self.macLabs = []
        self.sunLabs = []

    def showPage(self):
        self.dialog.show()
        self.listing.setVisible(False)

    def setXP(self):
        self.listing.setOs("Windows XP")
        self.listing.setVisible(True)
        self.parse()

    def setMac(self):
        self.listing.setOs("Macintosh")
        self.listing.setVisible(True)
        self.parse()

    def setSun(self):
        self.listing.setOs("Sun Solaris")
        self.listing.setVisible(True)
        self.parse()

    def parse(self):
        print "hey"

class ComputerLab():
    def __init__(self, room, num, time):
        self.room = room
        self.num = num
        self.time = time

    def __repr__(self):
        tab="&nbsp;&nbsp;&nbsp;&nbsp;"
        return "%s %s %s %s %s" % (self.room, tab, self.num, tab, self.time)

