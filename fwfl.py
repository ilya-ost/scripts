#!/usr/bin/python2.5

import os
import sys

list_dir = os.path.expanduser ('~/texts/English/range BNC/')

for f_path in os.listdir (list_dir):
    if not os.system ('cat "' + list_dir + f_path
                      + '" | grep -w ' + sys.argv[1] + '> /dev/null' ):
        print "Word found in ", f_path
    
