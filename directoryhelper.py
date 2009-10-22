from mechanize import Browser
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup
import sys, string
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DirectoryHelper():

    def __init__(self, dialog, form):
        self.dialog = dialog
        self.form = form
        sb = self.form.searchButton
        self.resultListBox = self.form.results
        self.fn = self.form.fnField
        self.ln = self.form.lnField
        self.listing = self.form.listing
        self.resultsList = []

    def showPage(self):
        self.listing.setVisible(False)
        self.resultListBox.setVisible(False)
        self.resultListBox.updateModel(QStandardItemModel())
        self.dialog.show()
        self.fn.clear()
        self.ln.clear()

    def populateResultsList(self):
        self.resultListBox.setVisible(True)
        model = QStandardItemModel()

        #generate background gradient
        grad = QLinearGradient(0,0,0,75)
        grad.setColorAt(0, QColor('gray'))
        grad.setColorAt(1, QColor('black'))

        for person in self.resultsList:
            item = QStandardItem('%s' % person.name)
            item.setForeground(QColor('gold'))
            item.setBackground(grad)
            item.setSizeHint(QSize(400,50))
            item.setTextAlignment(Qt.AlignCenter)
            item.setFont(QFont(QString('helvetica'), 12, 75, False))
            item.setEditable(False)
            model.appendRow(item)
        self.resultListBox.updateModel(model)

    def doSearch(self):
        del self.resultsList
        self.resultsList = []
        self.listing.setVisible(False)
        self.resultListBox.setVisible(False)
        self.thread = ThreadedDirectoryParser(self.fn.text(), \
                                    self.ln.text(), self.resultsList)
        self.dialog.connect(self.thread, SIGNAL("done()"), \
                                    self.populateResultsList)

    def displayInfo(self, index):
        self.listing.setVisible(True)
        self.listing.setListing(self.resultsList[index.row()])

class DirectoryResult():
    def __init__(self, name, email, phone, addr, univ):
        self.name = name
        self.email = email
        self.phone = phone
        self.addr = addr.replace("$", "<br>")
        self.univ = univ

    def __repr__(self):
        return "Name: %s\nEmail: %s\nPhone: %s\nAddress: %s\nSchool: %s\n" \
                %(self.name, self.email, self.phone, \
                    self.addr.replace("<br>","\n"), self.univ)

class ThreadedDirectoryParser(QThread):
    def __init__(self, fn, ln, res, parent = None):
        QThread.__init__(self, parent)
        self.first = fn
        self.last = ln
        self.resultsList = res
        self.start()

    def run(self):
        self.parseResults()

    def parseResults(self):
        mech = Browser()
        mech.addheaders = [ ('User-agent', 'Mozilla/5.0 (compatible)') ]
        mech.set_handle_robots(False)
        url = "http://web.ics.purdue.edu/~mdswanso/dir.php?ln=%s&fn=%s" % \
                    (self.last, self.first)
        page = mech.open(url)
        html = page.read()
        soup = BeautifulStoneSoup(html)
        for item in soup.findAll('person'):
            name = item.find('name').contents[0]

            email = item.find('email')
            if (len(email.contents)):
                email = email.contents[0]
            else:
                email = "Not listed"

            phone = item.find('phone')
            if (len(phone.contents)):
                phone = phone.contents[0]
            else:
                phone = "Not listed"

            addr = item.find('addr')
            if (len(addr.contents)):
                addr = addr.contents[0]
            else:
                addr = "<br>Not listed"

            univ = item.find('univ')
            if (len(univ.contents)):
                univ = univ.contents[0]
            else:
                univ = "<br>Not listed"

            self.resultsList.append(DirectoryResult(name, email, phone, \
                                        addr, univ))
        self.emit(SIGNAL("done()"))

