from mechanize import Browser
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup
import sys, re, string
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#This module is responsible for displaying Purdue Campus news stories that
#are available through FeedBurner RSS feeds


class NewsHelper():

    def __init__(self, dialog, form):
        self.dialog = dialog
        self.form = form
        self.progressBar = form.progressBar
        self.loadingLabel = form.loadingLabel
        self.topicListBox = form.topicListBox
        self.headlineListBox = form.headlineListBox
        self.results = self.form.resultsField
        self.feedUrls = ['http://feeds.feedburner.com/PurdueStudentNews?format=xml', \
                        'http://feeds.feedburner.com/PurdueEngNews?format=xml', \
                        'http://feeds.feedburner.com/PurdueResearchNews?format=xml', \
                        'http://feeds.feedburner.com/PurdueBusinessNews?format=xml', \
                        'http://feeds.feedburner.com/PurdueEventNews?format=xml']
        self.topicList = ['Student', 'Engineering', 'Research', \
                         'Business', 'Events']
        self.headlineList = []
        self.newsList = []
        self.descList = []
        self.regex = re.compile('<!-- AddThis Button END.*AddThis Button BEGIN -->', re.M | re.S)
        self.regex2 = re.compile('<TABLE.*</table>', re.M | re.S)
        self.mech = Browser()
        self.mech.addheaders = [ ('User-agent', 'Mozilla/5.0 (compatible)') ]
        self.mech.set_handle_robots(False)



    def showPage(self):
        self.hideContent()
        self.dialog.show()
        #self.results.clear()
        self.thread = ThreadedNewsParser(self.newsList, \
                                         self.headlineList, \
                                         self.descList)
        self.dialog.connect(self.thread, SIGNAL("done()"), self.populateTopicList)
        self.dialog.connect(self.thread, SIGNAL("show()"), self.showContent)
        #self.parseFeeds()
        #self.initializeNews()

    def close(self):
        self.dialog.close()

    def showContent(self):
        self.form.homeButton.setVisible(True)
        self.progressBar.setVisible(False)
        self.loadingLabel.setVisible(False)
        self.topicListBox.setVisible(True)
        self.headlineListBox.setVisible(True)
        self.results.setVisible(True)

    def hideContent(self):
        self.form.homeButton.setVisible(False)
        self.progressBar.setVisible(True)
        self.loadingLabel.setVisible(True)
        self.topicListBox.setVisible(False)
        self.headlineListBox.setVisible(False)
        self.results.setVisible(False)

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
                descriptions.append(story.link)
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
        page = self.mech.open('%s' % self.descList[0][0])
        html = page.read()
        article = self.regex.search(html).group()
        self.results.setHtml(QString('%s' % self.regex2.sub('', article)))

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
        self.initializeNews()

    def displayStory(self, index):
        index=index.row()
        index2=self.topicListBox.selectedIndexes()
        if len(index2) > 0:
            index2 = index2[0].row()
        else:
            index2 = 0
        page = self.mech.open('%s' % self.descList[index2][index])
        html = page.read()
        article = self.regex.search(html).group()
        self.results.setHtml(QString('%s' % self.regex2.sub('', article)))

class NewsStory():
    def __init__(self, date, title, link, desc):
        self.date=date
        self.title=title
        self.link=link
        self.desc=desc

    def display(self):
        print self.title
        print

class ThreadedNewsParser(QThread):
    def __init__(self, nl, hl, dl, parent = None):
        QThread.__init__(self, parent)
        self.exiting = False
        self.newsList = nl
        self.headlineList = hl
        self.descList = dl
        self.feedUrls = ['http://feeds.feedburner.com/PurdueStudentNews?format=xml', \
                        'http://feeds.feedburner.com/PurdueEngNews?format=xml', \
                        'http://feeds.feedburner.com/PurdueResearchNews?format=xml', \
                        'http://feeds.feedburner.com/PurdueBusinessNews?format=xml', \
                        'http://feeds.feedburner.com/PurdueEventNews?format=xml']
        self.start()

    def run(self):
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
                descriptions.append(story.link)
                #story.display()
            self.headlineList.append(headlines)
            self.descList.append(descriptions)
        #self.populateTopicList()
        self.emit(SIGNAL("done()"))
        self.emit(SIGNAL("show()"))


