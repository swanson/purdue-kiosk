import poplib, email
import sys, string, threading, time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from hid import *

class EmailHelper():

    def __init__(self, dialog, form):
        self.dialog = dialog
        self.form = form
        self.subjectListBox = form.subjectListBox
        self.messageDisplay = form.messageDisplay
        self.userNameField = form.userNameField
        self.passwordField = form.passwordField
        self.progressBar = form.progressBar
        self.subjectList = []
        self.bodyList = []
        self.database = {0x0016131238:'mdswanso'} #add all users here

    def showPage(self):
        self.dialog.show()
        self.listener = USBListener("0007","1337") #use real vendor/product
        self.dialog.connect(self.listener, SIGNAL("foundPUID"), self.lookupPUID)
        self.listener.start()

    def lookupPUID(self, id):
        print "looking for %i" % id
        self.userNameField.setText("%s" % self.database[id])

    def close(self):
        self.dialog.close()
        self.listener.cleanup()

    def checkEmail(self):
        self.progressBar.setVisible(True)
        self.progressBar.setValue(1)
        self.thread = ThreadedEmailParser(self.userNameField.text(), \
                                    self.passwordField.text(), \
                                    self.subjectList, self.bodyList,
                                    self.progressBar)
        self.dialog.connect(self.thread, SIGNAL("done()"), self.populateSubjectList)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(1)

    def populateSubjectList(self):
        self.progressBar.setVisible(False)
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
        self.progressBar.setVisible(False)

    def displayEmail(self, index):
        index=index.row()
        self.messageDisplay.setVisible(True)
        self.messageDisplay.setHtml(QString('%s' % self.bodyList[index]))

    def loadMessages(self):
        username = self.userNameField.text()
        password = self.passwordField.text()
        mailserver = poplib.POP3_SSL('%s.mail.purdue.edu' % username)
        mailserver.user(username)
        mailserver.pass_(password)
        numMessages = len(mailserver.list()[1])
        z=0
        messageLimit = 15
        for i in reversed(range(numMessages)):
            message = ""
            z += 1
            if (z > messageLimit):
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
                        break
                    if part.get_content_type() == 'text/html':
                        message += "<br>" + part.get_payload().replace("\n", "<br>") \
                                     + "<br>"
                        break
            else:
                message += "<br>" + mail.get_payload().replace("\n", "<br>") + "<br>"

            self.bodyList.append(message)
            self.progressBar.setValue(float(z) / float(messageLimit) * 100)

class ThreadedEmailParser(QThread):
    def __init__(self, username, pw, sl, bl, pb, parent = None):
        QThread.__init__(self, parent)
        self.exiting = False
        self.user = username
        self.pw = pw
        self.subjectList = sl
        self.bodyList = bl
        self.progressBar = pb
        self.start()

    def run(self):
        self.parseMessages()

    def parseMessages(self):
        mailserver = poplib.POP3_SSL('%s.mail.purdue.edu' % self.user)
        mailserver.user(self.user)
        mailserver.pass_(self.pw)
        numMessages = len(mailserver.list()[1])
        z=0
        messageLimit = 15
        for i in reversed(range(numMessages)):
            message = ""
            z += 1
            if (z > messageLimit):
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
                        break
                    if part.get_content_type() == 'text/html':
                        message += "<br>" + part.get_payload().replace("\n", "<br>") \
                                     + "<br>"
                        break
            else:
                message += "<br>" + mail.get_payload().replace("\n", "<br>") + "<br>"

            self.bodyList.append(message)
        self.emit(SIGNAL("done()"))

class USBListener(QThread):
    def __init__(self, vendor, product, parent = None):
        QThread.__init__(self, parent)
        self.vendor = vendor
        self.product = product
        self.running = 1
        self.setupHIDListener()

    def run(self):
        self.listen()

    def setupHIDListener(self):
        ret = hid_init()
        if ret != HID_RET_SUCCESS:
            sys.stderr.write("hid_init failed with return code %d.\n" % ret)

        self.hid = hid_new_HIDInterface()
        self.matcher = HIDInterfaceMatcher()

        ret = hid_force_open(self.hid, 0, self.matcher, 3)
        if ret != HID_RET_SUCCESS:
            sys.stderr.write("hid_force_open failed with return code %d.\n" % ret)

    def cleanup(self):
        self. running = 0
        ret = hid_close(self.hid)
        if ret != HID_RET_SUCCESS:
            sys.stderr.write("hid_close failed with return code %d.\n" % ret)
        hid_cleanup()

    def int32(self, x):
        if x>0xFFFFFFFF:
            raise OverflowError
        if x>0x7FFFFFFF:
            x=int(0x100000000-x)
        if x<2147483648:
            return -x
        else:
            return -2147483648
        return x

    def listen(self):
        print "listening for hid at %s:%s" % (self.vendor, self.product)
        #remove hard-coded test values
        endpoint = self.int32(0xff9c0001)
        puid = 0x0016131238
        ret = 0
        while self.running:
            #implement interrupt reading
            #ret, bytes = hid_interrupt_read(self.hid, endpoint, 1, 10)
            #mag reader sends interrupts
            #byte 0 - status
            #byte 1 - 4 : 32bit int - PUID
            if ret != HID_RET_SUCCESS:
                sys.stderr.write("hid_get_input_report failed with return code %d.\n" % ret)
            else:
                self.emit(SIGNAL("foundPUID"), puid)
                print "scanned %i" % puid
                ret = 1

            time.sleep(1)
