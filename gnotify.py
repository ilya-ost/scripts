#! /usr/bin/env python

import gmailatom
import time
import sys
import os

username="ilya.a.ostanin@gmail.com"
password="1JksX19CvhEp"

try:
    connection = gmailatom.GmailAtom(username, password)
    #         print "connect"
    connection.refreshInfo()
    #         print "refresh info"
    unread = connection.getUnreadMsgCount()
    if unread > 0:
        print "Gmail:", unread
        sys.stdout.flush()
    else:
        print
        sys.stdout.flush()
except:
    print
    sys.stdout.flush()
        
    #         print "connection error"
    
