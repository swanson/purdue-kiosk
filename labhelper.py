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
        self.xpButton = self.form.xpButton
        self.macButton = self.form.macButton
        self.sunButton = self.form.sunButton
        self.loadingLabel = self.form.loadingLabel
        self.progressBar = self.form.progressBar
        self.help = self.form.instructions

    def showPage(self):
        self.xp = []
        self.mac = []
        self.sun = []
        self.labs = [self.xp, self.mac, self.sun]

        self.dialog.show()
        self.hideContent()
        self.listing.setVisible(False)
        #self.parse()
        self.thread = ThreadedLabParser(self.labs)
        self.dialog.connect(self.thread, SIGNAL("done()"), self.showContent)

    def close(self):
        self.dialog.close()

    def showContent(self):
        self.form.homeButton.setVisible(True)
        self.progressBar.setVisible(False)
        self.loadingLabel.setVisible(False)
        self.xpButton.setVisible(True)
        self.macButton.setVisible(True)
        self.sunButton.setVisible(True)
        self.help.setVisible(True)

    def hideContent(self):
        self.form.homeButton.setVisible(False)
        self.progressBar.setVisible(True)
        self.loadingLabel.setVisible(True)
        self.xpButton.setVisible(False)
        self.macButton.setVisible(False)
        self.sunButton.setVisible(False)
        self.help.setVisible(False)

    def setXP(self):
        self.listing.setOs("Windows XP")
        self.listing.setIcon("xp")
        self.listing.setVisible(True)
        self.dumpResults(self.xp)

    def setMac(self):
        self.listing.setOs("Macintosh")
        self.listing.setIcon("mac")
        self.listing.setVisible(True)
        #self.parse()
        self.dumpResults(self.mac)

    def setSun(self):
        self.listing.setOs("Sun Solaris")
        self.listing.setIcon("sun")
        self.listing.setVisible(True)
        #self.parse()
        self.dumpResults(self.sun)

    def dumpResults(self, list):
        #self.listing.setLabs(list[1].display())
        str = "<table>"
        i = 0
        for lab in list:
            if (i == 0):
                i = 1
                continue
            str += "<tr>" + lab.display() + "</tr>"
        str += "</table>"
        self.listing.setLabs(str)

    def parse(self):
        url = "https://tomcat.itap.purdue.edu:8445/ICSWeb/AvailableStations"
        page = urllib.urlopen(url)
        soup = BeautifulSoup(page.read())
        i=0
        j=0
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
        str = "<td width='200'>%s</td> <td width='100'>%s</td> <td>%s</td>" \
                        % (self.room, self.num, self.time)
        return str

class ThreadedLabParser(QThread):
    def __init__(self, labs, parent = None):
        QThread.__init__(self, parent)
        self.labs = labs
        self.start()

    def run(self):
        self.parseLabOpenings()

    def parseLabOpenings(self):
        url = "https://tomcat.itap.purdue.edu:8445/ICSWeb/AvailableStations"
        page = urllib.urlopen(url)
        soup = BeautifulSoup(page.read())
        i=0
        j=0
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

        self.emit(SIGNAL("done()"))

