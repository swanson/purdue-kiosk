from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import sys
from PyQt4 import *

class NewsHelper():

    def __init__(self, dialog, form):
        self.dialog = dialog
        self.form = form
        sb = self.form.searchButton
        self.results = self.form.resultsField
        
    def showPage(self):
        self.dialog.show()
        self.results.clear()

    def doSearch(self):
        mech = Browser()
        mech.addheaders = [ ('User-agent', 'Mozilla/5.0 (compatible)') ]
        mech.set_handle_robots(False)
        url = "http://www.purdue.edu/newsroom/"
        page = mech.open(url)
        html = page.read()
        soup = BeautifulSoup(html)
        self.results.setText(soup.prettify())
