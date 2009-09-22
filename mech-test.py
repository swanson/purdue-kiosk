from mechanize import Browser
from BeautifulSoup import BeautifulSoup, SoupStrainer
import re

mech = Browser()
mech.addheaders = [ ('User-agent', 'Mozilla/5.0 (compatible)') ]
mech.set_handle_robots(False)
url = "http://mobile.rivals.com/schedule.asp?Team=PURDUE&Sport=1"
page = mech.open(url)
html = page.read()
tbl = SoupStrainer('table')
soup = BeautifulSoup(html)
schedule = soup.find('font')
table = schedule.find('table')
i=0
for line in table.findAll('tr'):
    if (i==0):
        i=1 #ghetto skip heading
    else:
        test=line.findAll('td')
        test2= test[2].find('font')
        vic = ""+test2.contents[0].string
        print vic
        if (vic[0] == u'W'):
            print "Win!"
        else:
            print "Lost!"
        date=line.find('font')
        print 'Date: %s' % date.string
        links=line.findAll('a')
        print 'Oppt: %s' % links[0].string
        if (len(links) > 1):
            print 'Score: %s' % links[1].string
        else:
            tds=line.findAll('td')
            print 'Time: %s' % tds[3].string
        print
