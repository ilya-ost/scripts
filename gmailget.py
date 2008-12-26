#! /usr/bin/env python

import gmailatom
import time
import sys

username="ilya.a.ostanin@gmail.com"


try:
    connection = gmailatom.GmailAtom(username, password)
#         print "connect"
    connection.refreshInfo()
#         print "refresh info"
    unread = connection.getUnreadMsgCount()
    for i in xrange(unread):
        print "No: \t\t", i
        print "Title: \t\t", connection.getMsgTitle(i)
        print "Summary: \t", connection.getMsgSummary(i)
        print "Author: \t", connection.getMsgAuthorName(i)
        print

except:
    print "Error!"
    
#         print "connection error"
    
