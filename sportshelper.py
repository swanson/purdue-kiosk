from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import sys
from PyQt4 import *

class SportsHelper():

    def __init__(self, dialog, form):
        self.dialog = dialog
        self.form = form
        self.scoreboard_1 = self.form.score1
        self.scoreboard_2 = self.form.score2
        self.scoreboard_3 = self.form.score3
        self.leftIndex = 0
        self.middleIndex = 1
        self.rightIndex = 2
        self.scorelist = []

    def showPage(self):
        self.dialog.show()
        del self.scorelist
        self.scorelist = []
        self.doSearch()
        self.leftIndex = 0
        self.middleIndex = 1
        self.rightIndex = 2

    def shiftRight(self):
        if (self.rightIndex < 11):
            self.leftIndex += 1
            self.middleIndex += 1
            self.rightIndex += 1
            self.setWidgets()

    def shiftLeft(self):
        if (self.leftIndex > 0):
            self.leftIndex -= 1
            self.middleIndex -= 1
            self.rightIndex -= 1
            self.setWidgets()
        
    def setWidgets(self):
        self.scorelist[self.leftIndex].setWidget(self.scoreboard_1)
        self.scorelist[self.middleIndex].setWidget(self.scoreboard_2)
        self.scorelist[self.rightIndex].setWidget(self.scoreboard_3)

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
            if (i==0):
                i=1 #ghetto skip table headings
            else:
                date=line.find('font')
                #print 'Date: %s' % date.string
                #self.scoreboard.setDate(str(date.string))
                links=line.findAll('a')
                #print 'Oppt: %s' % links[0].string
                #self.scoreboard.setAwayTeam(str(links[0].string))
                opp = links[0].string
                if (len(links) > 1):
                    #print 'Score: %s' % links[1].string
                    scores=links[1].string.split('-')
                    #self.scoreboard.setHomeScore(str(scores[0]))
                    #self.scoreboard.setAwayScore(str(scores[1]))
                    tds=line.findAll('td')
                    hl='Record: %s' % str(tds[3].string)
                    gameScore = FootballScore(str(date.string), str(opp), \
                        str(scores[0]), str(scores[1]), str(hl))
                else:
                    tds=line.findAll('td')
                    #print 'Time: %s' % tds[3].string
                    #self.scoreboard.setHeadline(str(tds[3].string))
                    gameScore = FootballScore(str(date.string), str(opp), \
                        '-', '-', str(tds[3].string))
                #test.setWidget(self.scoreboard)
                self.scorelist.append(gameScore)
        self.setWidgets()

class FootballScore():
    def __init__(self, date, opp, homescore, awayscore, headline=''):
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
        w.setHeadline(self.headline)
        
