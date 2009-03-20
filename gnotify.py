#! /usr/bin/env python

import gmailatom
import time
import sys
import os
import pynotify

username="ilya.a.ostanin@gmail.com"
password="1JksX19CvhEp"

show = len(sys.argv) == 2 and sys.argv[1] == 'show'

# print show


try:
    connection = gmailatom.GmailAtom(username, password)
    #         print "connect"
    connection.refreshInfo()
    #         print "refresh info"
    unread = connection.getUnreadMsgCount()
    if unread > 0 or show:
        # print "Gmail:", unread
        if pynotify.init("My Application Name"):
            n = pynotify.Notification("Gmail", "%d new messages" % unread)
            n.show()
        # sys.stdout.flush()
    else:
        pass
        # print
        # sys.stdout.flush()
except:
    print
    sys.stdout.flush()
        
    #         print "connection error"
    
