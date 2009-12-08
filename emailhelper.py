import poplib, email
import sys, string, threading, time, socket, os
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
        self.loadingLabel = form.loadingLabel
        self.subjectList = []
        self.bodyList = []
        self.database = {1613123:'mdswanso', \
                         1618372:'jsweval', \
                         1640427:'tsafford', \
                         1621852:'zcurosh' } #add all users here

        self.listener = USBListener(0x03eb,0x204f, 1) #use real vendor/product
        self.dialog.connect(self.listener, SIGNAL("foundPUID"), self.lookupPUID)


    def showPage(self):
        self.dialog.show()
        self.userNameField.setText("")
        self.passwordField.setText("")
        self.subjectList = []
        self.subjectListBox.setVisible(False)
        self.messageDisplay.setVisible(False)
        self.loadingLabel.setVisible(False)
        self.listener.start()

    def lookupPUID(self, id):
        print "looking for %i" % id
        self.userNameField.setText("%s" % self.database[id])
        self.passwordField.setText("")
        self.subjectList = []
        self.subjectListBox.setVisible(False)
        self.messageDisplay.setVisible(False)

    def close(self):
        #self.listener.cleanup()
        self.dialog.close()


    def checkEmail(self):
        if len(self.userNameField.text()) < 1:
            return
        if len(self.passwordField.text()) < 1:
            return
        self.progressBar.setVisible(True)
        self.loadingLabel.setVisible(True)
        self.progressBar.setValue(1)
        self.thread = ThreadedEmailParser(self.userNameField.text(), \
                                    self.passwordField.text(), \
                                    self.subjectList, self.bodyList,
                                    self.progressBar)
        self.dialog.connect(self.thread, SIGNAL("done()"), self.populateSubjectList)
        self.dialog.connect(self.thread, SIGNAL("loginError"), self.handleError)
        self.thread.start()
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(1)

    def handleError(self):
        self.progressBar.setVisible(False)
        self.loadingLabel.setVisible(False)
        QMessageBox.critical(self.dialog, "Login Error", \
                "Your user name and/or password was incorrect!\nPlease try again.")


    def populateSubjectList(self):
        self.progressBar.setVisible(False)
        self.loadingLabel.setVisible(False)
        self.subjectListBox.setVisible(True)
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

class ThreadedEmailParser(QThread):
    def __init__(self, username, pw, sl, bl, pb, parent = None):
        QThread.__init__(self, parent)
        self.exiting = False
        self.user = username
        self.pw = pw
        self.subjectList = sl
        self.bodyList = bl
        self.progressBar = pb
        #self.start()

    def run(self):
        self.parseMessages()

    def parseMessages(self):
        try:
            mailserver = poplib.POP3_SSL('%s.mail.purdue.edu' % self.user)
        except socket.error:
            self.emit(SIGNAL("loginError"))
            return
        try:
            mailserver.user(self.user)
            mailserver.pass_(self.pw)
            numMessages = len(mailserver.list()[1])
        except poplib.error_proto:
            self.emit(SIGNAL("loginError"))
            return
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
    def __init__(self, vendor, product, intnum, parent = None):
        QThread.__init__(self, parent)
        self.vendor = vendor
        self.product = product
        self.interface_number = intnum
        self.setupHIDListener()

    def run(self):
        self.running = 1
        self.listen()

    def setupHIDListener(self):
        ret = hid_init()
        if ret != HID_RET_SUCCESS:
            sys.stderr.write("hid_init failed with return code %d.\n" % ret)

        self.hid = hid_new_HIDInterface()
        self.matcher = HIDInterfaceMatcher()
        self.matcher.vendor_id = self.vendor
        self.matcher.product_id = self.product

        ret = hid_force_open(self.hid, self.interface_number, self.matcher, 3)
        if ret != HID_RET_SUCCESS:
            sys.stderr.write("hid_force_open failed with return code %d.\n" % ret)

    def cleanup(self):
        self.running = 0
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
        while self.running:
            ret, bytes = hid_interrupt_read(self.hid, 0x82, 5, 1000)
            if ret != HID_RET_SUCCESS and ret != HID_RET_FAIL_INT_READ:
                sys.stderr.write("hid_interrupt_read failed with return code %d.\n" % ret)
            elif ret != HID_RET_FAIL_INT_READ:
                puid = 0
                for i in range(4,0,-1):
                    puid <<= 8
                    puid += ord(bytes[i])

                if (puid != 0):
                    self.emit(SIGNAL("foundPUID"), puid)
            time.sleep(1)
