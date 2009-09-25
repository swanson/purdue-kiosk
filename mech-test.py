from mechanize import Browser
from BeautifulSoup import BeautifulSoup, SoupStrainer, BeautifulStoneSoup
import re
import urllib

class NewsStory():
    def __init__(self, date, title, link, desc):
        self.date=date
        self.title=title
        self.link=link
        self.desc=desc

    def display(self):
        print self.title, self.date, self.link, self.desc
        print
        print

mech = Browser()
mech.addheaders = [ ('User-agent', 'Mozilla/5.0 (compatible)') ]
mech.set_handle_robots(False)
url = "http://feeds.feedburner.com/PurdueEngNews?format=xml"
page = mech.open(url)
html = page.read()
soup = BeautifulStoneSoup(html)
newsList = []

for item in soup.findAll('item'):
    date = item.find('pubdate')
    title = item.find('title')
    link = item.find('link')
    desc = item.find('description')
    if (len(title.contents) > 0):
        title2 = title.contents[0]
    else:
        title2 = 'None'
    newsList.append(NewsStory(date.contents[0], title2, link.contents[0], \
        desc.contents[0]))

for story in newsList:
    story.display()
    


