from mechanize import Browser
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class NewsHelper():

    def __init__(self, dialog, form):
        self.dialog = dialog
        self.form = form
        self.topicListBox = form.topicListBox
        self.headlineListBox = form.headlineListBox
        self.results = self.form.resultsField
        self.feedUrls = ['http://feeds.feedburner.com/PurdueStudentNews?format=xml', \
                        'http://feeds.feedburner.com/PurdueEngNews?format=xml', \
                        'http://feeds.feedburner.com/PurdueResearchNews?format=xml', \
                        'http://feeds.feedburner.com/PurdueBusinessNews?format=xml', \
                        'http://feeds.feedburner.com/PurdueEventNews?format=xml']
        self.topicList = ['Student News', 'Engineering News', 'Research News', \
                         'Business News', 'Events']
        self.headlineList = []
        self.newsStoryList = []
        
        
    def showPage(self):
        self.dialog.show()
        self.results.clear()
        self.parseFeeds()
        
    def parseFeeds(self):
        mech = Browser()
        mech.addheaders = [ ('User-agent', 'Mozilla/5.0 (compatible)') ]
        mech.set_handle_robots(False)
        for url in self.feedUrls:
        #url = "http://feeds.feedburner.com/PurdueEngNews?format=xml"
            page = mech.open(url)
            html = page.read()
            soup = BeautifulStoneSoup(html)
            newsList = []
            headlines = []
            i=0
            for item in soup.findAll('item'):
                if (i > 20):
                    break
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
                i+=1
            for story in newsList:
                headlines.append(story.title)
                #story.display()
            self.headlineList.append(headlines)
        self.populateTopicList()        

    def populateHeadlineList(self, index):
        index = index.row()
        model = QStandardItemModel()
        
        #generate background gradient
        grad = QLinearGradient(0,0,0,75)
        grad.setColorAt(0, QColor('gray'))
        grad.setColorAt(1, QColor('black'))

        for headline in self.headlineList[index]:                   
            item = QStandardItem('%s' % headline)
            item.setForeground(QColor('gold'))
            item.setBackground(grad)
            item.setSizeHint(QSize(200,50))
            item.setTextAlignment(Qt.AlignCenter)
            item.setFont(QFont(QString('helvetica'), 12, 75, False))
            item.setEditable(False)
            model.appendRow(item)
        self.headlineListBox.updateModel(model)

    def populateTopicList(self):
        model = QStandardItemModel()
        
        #generate background gradient
        grad = QLinearGradient(0,0,0,75)
        grad.setColorAt(0, QColor('gray'))
        grad.setColorAt(1, QColor('black'))

        for topic in self.topicList:                   
            item = QStandardItem('%s' % topic)
            item.setForeground(QColor('gold'))
            item.setBackground(grad)
            item.setSizeHint(QSize(200,50))
            item.setTextAlignment(Qt.AlignCenter)
            item.setFont(QFont(QString('helvetica'), 12, 75, False))
            item.setEditable(False)
            model.appendRow(item)
        self.topicListBox.updateModel(model)
 

class NewsStory():
    def __init__(self, date, title, link, desc):
        self.date=date
        self.title=title
        self.link=link
        self.desc=desc

    def display(self):
        print self.title
        print

