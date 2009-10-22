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
        self.listing = self.form.listing

    def showPage(self):
        self.dialog.show()
        self.listing.setVisible(False)

    def setXP(self):
        self.listing.setOs("Windows XP")
        self.listing.setVisible(True)
        self.parse()
        self.dumpResults(self.xp)

    def setMac(self):
        self.listing.setOs("Macintosh")
        self.listing.setVisible(True)
        self.parse()
        self.dumpResults(self.mac)

    def setSun(self):
        self.listing.setOs("Sun Solaris")
        self.listing.setVisible(True)
        self.parse()
        self.dumpResults(self.sun)

    def dumpResults(self, list):
        #self.listing.setLabs(list[1].display())
        str = ""
        i = 0
        for lab in list:
            if (i == 0):
                i = 1
                continue
            str += lab.display() + "<br>"
        self.listing.setLabs(str)

    def parse(self):
        url = "https://tomcat.itap.purdue.edu:8445/ICSWeb/AvailableStations"
        page = urllib.urlopen(url)
        soup = BeautifulSoup(page.read())
        i=0
        j=0
        self.xp = []
        self.mac = []
        self.sun = []
        self.labs = [self.xp, self.mac, self.sun]
        for tbl in soup.findAll('table'):
            if (i==0):
                i=1
                continue	
            for tr in tbl.findAll('tr'):
                if (len(tr.contents) > 2):
                    a = ComputerLab(None, None, None)
                    a.room = tr.contents[0].find('font').contents[0]
                    a.num = tr.contents[1].find('font').contents[0]
                    a.time = tr.contents[2].find('font').contents[0]
                    self.labs[j].append(a)
        j+=1

class ComputerLab():
    def __init__(self, room, num, time):
        self.room = room
        self.num = num
        self.time = time

    def display(self):
        tab = "&nbsp;&nbsp;&nbsp;&nbsp;"
        str = "%s %s %s %s %s" % (self.room, tab, self.num, tab, self.time)
        return str
