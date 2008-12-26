#! /usr/bin/env python2.5

import os
import sys

if len (sys.argv) < 5 :
    print "usage: getlist url1 base url2 end [dir]"
    exit (1)
else:
    url1 = sys.argv[1]
    base = sys.argv[2]
    url2 = sys.argv[3]
    end = int (sys.argv[4])
    dir = "~/downloads/"
    if len (sys.argv) > 5 :
        dir = sys.argv[5]

beg = int (base)
for i in range (beg, end + 1) :
    if len (base) == 1 :
        numstr = str (i)
    else:
        numstr = "0" * (len(base) - len(str(i))) + str (i)

    print "*" * 10, "getting" , i, "*" * 10
#     print url1 + numstr + url2
    os.system ("wget -P " + dir + " "  + url1 + numstr + url2 )

