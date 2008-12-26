#!/usr/bin/env python2.5

import sys
import os
import re

if len(sys.argv) == 3:
    in_name = sys.argv[1]
    time = int(sys.argv[2])
else:
    print "usage: srttime.py filename time"
    exit(1)

in_file = open(in_name, "r")
out_file = open(in_name + "-time(%d)" % time, "w")

def time_str2int(time_str):
    return 3600000 * int(time_str[0:2]) + 60000 * int(time_str[3:5]) + 1000 * int(time_str[6:8]) + int(time_str[9:12])

def time_int2str(time_int):
    hrs = time_int / 3600000
    time_int -= hrs * 3600000
    mins = time_int / 60000
    time_int -= mins * 60000
    secs = time_int / 1000
    msecs = time_int - secs * 1000
    return "%02d:%02d:%02d,%d" % (hrs, mins, secs, msecs)

for in_line in in_file.xreadlines():
    out_line = in_line.strip()
    if re.search("-->", out_line):
        out_line = "%s --> %s" % tuple(map(lambda x: time_int2str(time_str2int(x) + time),
                                           re.split(" --> ", in_line)))
        print out_line
    out_file.write(out_line + "\n")

out_file.close()
