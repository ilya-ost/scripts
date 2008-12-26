#!/usr/bin/env python2.5

from __future__ import with_statement
import os
import glob
import re
import shutil

gg = glob.iglob
ope = os.path.expanduser
opj = os.path.join

sdir = ope("~/downloads")
vdir = ope("~/downloads/torrents/House MD Season 3")

for s in gg(sdir + "/*.srt"):
    n = int(re.split("house", s)[1][1:3])
    v = filter(lambda x: re.match(r".*MD - %d.*" % (n), x),
               gg(vdir + "/*.avi"))[0].replace("avi", "srt")
    shutil.move(s, v)
    print s
    print v
    
