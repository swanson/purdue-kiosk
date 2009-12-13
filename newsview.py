from PyQt4 import QtCore, QtGui
from PyQt4.QtWebKit import *
from newshelper import *
import os
from flickcharm import *
from CustomListBox import *

#This module is responsible for displaying Purdue Campus news stories that
#are available through FeedBurner RSS feeds

class NewsView(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,1024,768).size()))
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0,0,1024,768))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setObjectName("frame")

        self.resultsField = QWebView(Dialog)
        self.resultsField.setGeometry(QtCore.QRect(450,85,500,590))
        self.resultsField.setTextSizeMultiplier(1.5)
        self.resultsField.setObjectName("resultsField")
        self.resultsField.settings().setAttribute(QWebSettings.AutoLoadImages, False)

        self.charm = FlickCharm()
        self.charm.activateOn(self.resultsField)

        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setGeometry(QRect(240, 350, 600, 100))
        self.progressBar.setVisible(False)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(1)

        self.loadingLabel = QLabel(Dialog)
        self.loadingLabel.setGeometry(QRect(240, 190, 600, 200))
        self.loadingLabel.setText("Loading news feeds...")
        self.loadingLabel.setAlignment(Qt.AlignCenter)

        self.topicListBox = CustomListBox(Dialog)
        self.topicListBox.setGeometry(QtCore.QRect(100,175,100,500))

        self.headlineListBox = CustomListBox(Dialog)
        self.headlineListBox.setGeometry(QtCore.QRect(215,175,225,500))

        self.homeButton= QPushButton(Dialog)
        self.homeButton.setGeometry(QRect(10,680,80,80))
        self.homeButton.setVisible(False)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.helper = NewsHelper(Dialog, self)
        self.topicListBox.connect(self.topicListBox, SIGNAL("clicked(QModelIndex)"), \
                                    self.helper.populateHeadlineList)
        self.headlineListBox.connect(self.headlineListBox, SIGNAL("clicked(QModelIndex)"), \
                                        self.helper.displayStory)
        self.homeButton.connect(self.homeButton, SIGNAL("clicked()"), self.helper.close)


    def retranslateUi(self, Dialog):
        path = os.getcwd()
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Campus News", None, QtGui.QApplication.UnicodeUTF8))
        Dialog.setStyleSheet(QtGui.QApplication.translate("Dialog", "", None, QtGui.QApplication.UnicodeUTF8))
        self.frame.setStyleSheet(QtGui.QApplication.translate("Dialog", "background-image: url(" + path + "/images/mockup_blank_template.png); background-repeat:no-repeat;", None, QtGui.QApplication.UnicodeUTF8))
        self.loadingLabel.setStyleSheet(QtGui.QApplication.translate("MainWindow", "font-size: 50px;", None, QtGui.QApplication.UnicodeUTF8))
        self.homeButton.setStyleSheet(QApplication.translate("MainWindow", "background-image: url(" + path + "/images/home.png); background-repeat:no-repeat;\n"
        "border-radius: 10px;", None, QApplication.UnicodeUTF8))


