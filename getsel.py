#! /usr/bin/env python

import sys
import os
import pynotify

buffile = os.path.expanduser ('~/.selbuf')
bufsize = 5


n = pynotify.Notification("Title", "body", "dialog-warning")
n.set_urgency(pynotify.URGENCY_NORMAL)
n.set_timeout(pynotify.EXPIRES_NEVER)
n.show()

if os.path.isfile (buffile):
    f = open (buffile, "r")
    buf = f.readlines ()
    f.close ()
    sel = buf [len (buf) - 1]
    buf [1:] = buf [:len (buf)-1]
    buf [0] = sel
    f = open (buffile, "w")
    for str in buf:
        f.write (str)
#         print str,
    f.close ()
    sys.stdout.write (sel[:len (sel)-1])
    os.system ("killall kdialog")
