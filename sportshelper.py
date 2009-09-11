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
       url = "http://mobile.rivals.com/schedule.asp?Team=PURDUE&Sport=1"
       page = mech.open(url)
       html = page.read()
       soup = BeautifulSoup(html)
       schedule = soup.find('font')
       table = schedule.find('table')
       i=0
        #todo - make list of all parsed results, stick the first one into the scoreboard
       for line in table.findAll('tr'):
        if (i!=1):
            i+=1 #ghetto skipping
        else:
            i+=1
            date=line.find('font')
            #print 'Date: %s' % date.string
            #self.scoreboard.setDate(str(date.string))
            links=line.findAll('a')
            #print 'Oppt: %s' % links[0].string
            #self.scoreboard.setAwayTeam(str(links[0].string))
            if (len(links) > 1):
                #print 'Score: %s' % links[1].string
                scores=links[1].string.split('-')
             #   self.scoreboard.setHomeScore(str(scores[0]))
             #   self.scoreboard.setAwayScore(str(scores[1]))
            else:
                tds=line.findAll('td')
            #    print 'Time: %s' % tds[3].string
            #    self.scoreboard.setHeadline(str(tds[3].string))
            #print
            test = FootballScore(str(date.string), str(links[0].string), \
                str(scores[0]), str(scores[1]))
            test.setWidget(self.scoreboard)

class FootballScore():
    def __init__(self, date, opp, homescore, awayscore, headline=None):
        self.date = date
        self.opponent = opp
        self.homescore = homescore
        self.awayscore = awayscore
        self.headline = headline

    def setWidget(self, w):
        w.setDate(self.date)
        w.setAwayTeam(self.opponent)
        w.setHomeScore(self.homescore)
        w.setAwayScore(self.awayscore)
        
