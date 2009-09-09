from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import sys
from PyQt4 import *

class DirectoryHelper():

    def __init__(self, dialog, form):
        self.dialog = dialog
        self.form = form
        sb = self.form.searchButton
        #sb.connect(sb, QtCore.SIGNAL("clicked()"), self.doSearch)
        self.results = self.form.resultsField
        self.fn = self.form.fnField
        self.ln = self.form.lnField
        
    def showDirectory(self):
        self.dialog.show()
        self.fn.clear()
        self.ln.clear()
        self.results.clear()

    def doSearch(self):
        mech = Browser()
        mech.addheaders = [ ('User-agent', 'Mozilla/5.0 (compatible)') ]
        mech.set_handle_robots(False)
        url = "http://web.ics.purdue.edu/~mdswanso/dir.php?ln=%s&fn=%s" % \
                    (self.ln.text(), self.fn.text())
        page = mech.open(url)
        html = page.read()
        soup = BeautifulSoup(html)
        self.results.setText(soup.prettify())
