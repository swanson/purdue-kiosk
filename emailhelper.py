import poplib, email
import sys, string
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class EmailHelper():

    def __init__(self, dialog, form):
        self.dialog = dialog
        self.form = form
        self.subjectListBox = form.subjectListBox
        self.messageDisplay = form.messageDisplay
        self.userNameField = form.userNameField
        self.passwordField = form.passwordField
        self.subjectList = []
        self.bodyList = []
        
    def showPage(self):
        self.dialog.show()
        #self.loadMessages()
        #self.populateSubjectList()

    def checkEmail(self):
        self.loadMessages()
        self.populateSubjectList()

    def populateSubjectList(self):
        model = QStandardItemModel()
        
        #generate background gradient
        grad = QLinearGradient(0,0,0,75)
        grad.setColorAt(0, QColor('gray'))
        grad.setColorAt(1, QColor('black'))

        for subject in self.subjectList:
            if (subject == ""):
                item = QStandardItem("No subject.")
            else:                   
                item = QStandardItem('%s' % subject)
            item.setForeground(QColor('gold'))
            item.setBackground(grad)
            item.setSizeHint(QSize(400,50))
            item.setTextAlignment(Qt.AlignCenter)
            item.setFont(QFont(QString('helvetica'), 12, 75, False))
            item.setEditable(False)
            model.appendRow(item)
        self.subjectListBox.updateModel(model)

    def displayEmail(self, index):
        index=index.row()
        self.messageDisplay.setHtml(QString('%s' % self.bodyList[index]))

    def loadMessages(self):
        username = self.userNameField.text()
        password = self.passwordField.text()
        mailserver = poplib.POP3_SSL('%s.mail.purdue.edu' % username)
        mailserver.user(username)
        mailserver.pass_(password)
        numMessages = len(mailserver.list()[1])
        z=0
        for i in reversed(range(numMessages)):
            message = ""
            z += 1
            if (z > 10):
                break
            msg = mailserver.retr(i+1)
            str = string.join(msg[1], "\n")
            mail = email.message_from_string(str)
    
            message += "From: " + mail["From"] + "<br>"
            message += "Subject: " + mail["Subject"] + "<br>"
            message += "Date: " + mail["Date"] + "<br>"
            self.subjectList.append(mail["Subject"])
    
            if mail.is_multipart():
                for part in mail.walk():
                    if part.get_content_type() == 'text/plain':
                        message += "<br>" + part.get_payload().replace("\n", "<br>") \
                                     + "<br>"
                    if part.get_content_type() == 'text/html':
                        message += "<br>" + part.get_payload().replace("\n", "<br>") \
                                     + "<br>"
            else:
                message += "<br>" + mail.get_payload().replace("\n", "<br>") + "<br>"
            
            self.bodyList.append(message)
