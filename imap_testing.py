from imaplib import *
import getpass
server= IMAP4_SSL("mdswanso.mail.purdue.edu")
server.login("mdswanso", getpass.getpass())
mboxes=server.list()[1]
#print mboxes
inbox=server.select()
type, data = server.search(None, 'ALL')
i=0;
messages=data[0].split(' ')
messages.reverse()
for num in messages:
    i+=1;
    if (i > 2):
        break;
    type, data = server.fetch(num, '(BODY[HEADER.FIELDS (Content-Type "text/plain" FROM SUBJECT DATE TEXT)])')
    #print data
    type2, data2 = server.fetch(num, '(BODY[TEXT])')
    print 'Message %s\n%s\n%s\n' % (num, data[0][1], data2[0][1])
    print '---------------------------------------------------------'
server.close()
server.logout()
