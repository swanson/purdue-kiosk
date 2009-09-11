from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import sys
from PyQt4 import *

class SportsHelper():

    def __init__(self, dialog, form):
        self.dialog = dialog
        self.form = form
        self.results = self.form.resultsDump        
        self.scoreboard = self.form.score1

    def showPage(self):
        self.dialog.show()
        self.results.clear()
        self.doSearch()

    def doSearch(self):
        mech = Browser()
        mech.addheaders = [ ('User-agent', 'Mozilla/5.0 (compatible)') ]
        mech.set_handle_robots(False)
        url = "http://m.espn.go.com/ncf/teamschedule?teamId=2509"
        page = mech.open(url)
        html = page.read()
        #soup = BeautifulSoup(html)
        #self.results.setText(soup.prettify())
        self.results.setText(html)
        self.scoreboard.setHomeScore("69")

class FootballScore():
    def __init__(self, date, opp, score, result):
        self.date = date
        self.opponent = opp
        self.score = score
        self.result = result
