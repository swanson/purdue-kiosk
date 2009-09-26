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
        self.newsList = []
        self.descList = []
        
        
    def showPage(self):
        self.dialog.show()
        self.results.clear()
        self.parseFeeds()
        self.initializeNews()
        
    def parseFeeds(self):
        mech = Browser()
        mech.addheaders = [ ('User-agent', 'Mozilla/5.0 (compatible)') ]
        mech.set_handle_robots(False)
        for url in self.feedUrls:
        #url = "http://feeds.feedburner.com/PurdueEngNews?format=xml"
            page = mech.open(url)
            html = page.read()
            soup = BeautifulStoneSoup(html)
            headlines = []
            descriptions = []
            i=0
            self.newsList = []
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
                self.newsList.append(NewsStory(date.contents[0], title2, link.contents[0], \
                    desc.contents[0]))
                i+=1
            for story in self.newsList:
                headlines.append(story.title)
                descriptions.append(story.desc)
                #story.display()
            self.headlineList.append(headlines)
            self.descList.append(descriptions)
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

    def initializeNews(self):
        model = QStandardItemModel()
        
        #generate background gradient
        grad = QLinearGradient(0,0,0,75)
        grad.setColorAt(0, QColor('gray'))
        grad.setColorAt(1, QColor('black'))

        for headline in self.headlineList[0]:                   
            item = QStandardItem('%s' % headline)
            item.setForeground(QColor('gold'))
            item.setBackground(grad)
            item.setSizeHint(QSize(200,50))
            item.setTextAlignment(Qt.AlignCenter)
            item.setFont(QFont(QString('helvetica'), 12, 75, False))
            item.setEditable(False)
            model.appendRow(item)
        self.headlineListBox.updateModel(model)
        self.results.setText('%s' % self.descList[0][0])



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
            item.setSizeHint(QSize(200,100))
            item.setTextAlignment(Qt.AlignCenter)
            item.setFont(QFont(QString('helvetica'), 12, 75, False))
            item.setEditable(False)
            model.appendRow(item)
        self.topicListBox.updateModel(model)
 
    def displayStory(self, index):
        index=index.row()
        index2=self.topicListBox.selectedIndexes()
        if len(index2) > 0:
            index2 = index2[0].row()
        else:
            index2 = 0
        self.results.clear()
        #print self.descList[index][index2]
        self.results.setText('%s' % self.descList[index2][index])

class NewsStory():
    def __init__(self, date, title, link, desc):
        self.date=date
        self.title=title
        self.link=link
        self.desc=desc

    def display(self):
        print self.title
        print

